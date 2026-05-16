#!/bin/bash
# Regenerate all audio for DeepEng using Edge TTS
# Fixed: rate parameter format (needs + sign for 0)

INPUT="/tmp/sentences.txt"
AUDIO_DIR="/mnt/d/hermes/deepeng/web/audio"
VOICE="zh-CN-YunjianNeural"
TOTAL=$(wc -l < "$INPUT")
COUNT=0

while IFS='|' read -r lesson sent_num en_text; do
    COUNT=$((COUNT + 1))
    lesson_dir="$AUDIO_DIR/lesson_$(printf '%02d' $lesson)"
    sent_file="$lesson_dir/sentence_$(printf '%02d' $sent_num).mp3"
    sent_slow="$lesson_dir/sentence_$(printf '%02d' $sent_num)_slow.mp3"
    
    mkdir -p "$lesson_dir"
    
    echo "[$COUNT/$TOTAL] L${lesson} S${sent_num}: ${en_text:0:40}"
    
    # Normal speed (no rate adjustment)
    edge-tts --voice "$VOICE" --text "$en_text" --write-media "$sent_file"
    if [ $? -ne 0 ]; then
        echo "  ERROR: normal speed failed"
    fi
    
    # Slow speed (-50% for noticeably slower)
    edge-tts --voice "$VOICE" --rate=-50% --text "$en_text" --write-media "$sent_slow"
    if [ $? -ne 0 ]; then
        echo "  ERROR: slow speed failed"
    fi
    
done < "$INPUT"

echo "=== SENTENCE AUDIO DONE ==="

# Generate full lesson audio
echo ""
echo "Generating full lesson audio..."
> /tmp/lesson_full.txt

while IFS='|' read -r lesson sent_num en_text; do
    echo -n "$en_text " >> "/tmp/lesson_${lesson}_full.txt"
done < "$INPUT"

for lesson in 1 2 3 4 5; do
    full_text=$(cat "/tmp/lesson_${lesson}_full.txt" | sed 's/ $//')
    lesson_dir="$AUDIO_DIR/lesson_$(printf '%02d' $lesson)"
    
    echo "Full L${lesson}: ${full_text:0:50}..."
    
    edge-tts --voice "$VOICE" --text "$full_text" --write-media "$lesson_dir/full.mp3"
    if [ $? -ne 0 ]; then
        echo "  ERROR: full audio failed"
    fi
    
    edge-tts --voice "$VOICE" --rate=-50% --text "$full_text" --write-media "$lesson_dir/full_slow.mp3"
    if [ $? -ne 0 ]; then
        echo "  ERROR: full slow audio failed"
    fi
done

echo "=== ALL DONE ==="
echo "Generated: $TOTAL sentences x 2 speeds + 10 full files"
