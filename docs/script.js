// Spotlight Effect Logic
function handleMouseMove(e) {
  const cards = document.getElementsByClassName("spotlight-card");
  for (const card of cards) {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    card.style.setProperty("--mouse-x", `${x}px`);
    card.style.setProperty("--mouse-y", `${y}px`);
  }
}

// Copy Install Command
function copyInstall() {
  navigator.clipboard.writeText('pip install CaesarCipher.extended');
  const toast = document.getElementById('copyToast');
  toast.style.opacity = '1';
  setTimeout(() => toast.style.opacity = '0', 2000);
}

function copyOutput() {
  const outputText = document.getElementById('demoOutput').textContent;
  navigator.clipboard.writeText(outputText);
  alert('Encrypted text copied!');
}

// Encryption Logic Port
// This logic mimics the Python backend exactly in JavaScript.
const input = document.getElementById('demoInput');
const output = document.getElementById('demoOutput');
const shiftSlider = document.getElementById('shiftRange');
const shiftValDisplay = document.getElementById('shiftVal');
const checkNum = document.getElementById('alterNumbers');
const checkSym = document.getElementById('alterSymbols');

function encryptText() {
  const text = input.value;
  const shift = parseInt(shiftSlider.value);
  const alterNumbers = checkNum.checked;
  const alterSymbols = checkSym.checked;

  shiftValDisplay.textContent = shift;

  const LOWERCASE = 97;
  const UPPERCASE = 65;
  const DIGIT = 48;

  let result = [];

  for (let i = 0; i < text.length; i++) {
    let char = text[i];
    let code = text.charCodeAt(i);

    // Lowercase
    if (code >= 97 && code <= 122) {
      result.push(String.fromCharCode((code - LOWERCASE + shift) % 26 + LOWERCASE));
    }
    // Uppercase
    else if (code >= 65 && code <= 90) {
      result.push(String.fromCharCode((code - UPPERCASE + shift) % 26 + UPPERCASE));
    }
    // Digits (if enabled)
    else if (code >= 48 && code <= 57 && alterNumbers) {
      result.push(String.fromCharCode((code - DIGIT + shift) % 10 + DIGIT));
    }
    // Symbols (if enabled)
    // Note: Logic matches Encryption.py 'not isalnum() and self.alterSymbols'
    else if (!((code >= 48 && code <= 57) || (code >= 65 && code <= 90) || (code >= 97 && code <= 122)) && alterSymbols) {
      try {
        result.push(String.fromCharCode(code + shift));
      } catch (e) {
        result.push(char);
      }
    } else {
      result.push(char);
    }
  }
  output.textContent = result.join('');
}

// Initialize Events
input.addEventListener('input', encryptText);
shiftSlider.addEventListener('input', encryptText);
checkNum.addEventListener('change', encryptText);
checkSym.addEventListener('change', encryptText);

// Run once on load
encryptText();