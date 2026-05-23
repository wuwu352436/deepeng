// Lazy-loaded lesson data: fetches lesson JSON files on-demand.
// Replaces the old static data.js with all 50 lessons embedded.

window.LESSONS = [];
window._lessonsReady = false;

(async function loadIndex() {
  try {
    const resp = await fetch('data/index.json');
    const index = await resp.json();
    window.LESSONS = index.map(item => ({
      id: item.id,
      title: item.title,
      _loaded: false
    }));
    window._lessonsReady = true;
    // If init is waiting, trigger it
    if (window._pendingInit) window._pendingInit();
  } catch (e) {
    console.error('Failed to load lesson index:', e);
    window._lessonsReady = true;
  }
})();

async function ensureLessonLoaded(idx) {
  const lesson = window.LESSONS[idx];
  if (!lesson || lesson._loaded) return;

  const lessonNum = String(lesson.id).padStart(3, '0');
  try {
    const resp = await fetch(`data/lesson_${lessonNum}.json`);
    const data = await resp.json();

    // Normalize: add 'questions' from 'quiz' for compatibility
    if (data.quiz && !data.questions) {
      data.questions = data.quiz.map(q => ({
        question_cn: q.question_cn,
        question_en: q.question_en || '',
        options: q.options,
        answer: q.answer
      }));
    }
    // Add sequential sentence IDs (old frontend expects them)
    data.sentences.forEach((s, i) => { if (s.id === undefined) s.id = i + 1; });

    data._loaded = true;
    window.LESSONS[idx] = data;
  } catch (e) {
    console.error(`Failed to load lesson ${lessonNum}:`, e);
  }
}
