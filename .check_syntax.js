const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf-8');
const m = html.match(/<script>([\s\S]+?)<\/script>/);
if (m) {
  try {
    new Function(m[1]);
    console.log('SYNTAX OK');
    process.exit(0);
  } catch(e) {
    console.log('SYNTAX ERROR:', e.message);
    process.exit(1);
  }
}
console.log('NO SCRIPT TAG FOUND');
