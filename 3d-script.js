let isRotating = false;
let rotationInterval;
let particlesEnabled = true;
let rotationSpeed = 5;
let currentScale = 100;

// 创建粒子效果
function createParticles() {
    const particlesContainer = document.getElementById('particles');
    for (let i = 0; i < 80; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.width = Math.random() * 6 + 3 + 'px';
        particle.style.height = particle.style.width;
        particle.style.animationDelay = Math.random() * 25 + 's';
        particle.style.animationDuration = (Math.random() * 15 + 15) + 's';
        particlesContainer.appendChild(particle);
    }
}

// 切换旋转
function toggleRotation() {
    const logo = document.getElementById('logo3d');
    const btn = document.getElementById('rotationBtn');
    
    if (isRotating) {
        clearInterval(rotationInterval);
        isRotating = false;
        btn.textContent = '开始旋转';
        btn.classList.remove('active');
    } else {
        rotationInterval = setInterval(() => {
            const currentTransform = logo.style.transform || '';
            const rotation = currentTransform.match(/rotateY\(([^)]+)\)/) || [0, '0deg'];
            const currentAngle = parseInt(rotation[1]) || 0;
            logo.style.transform = `rotateY(${currentAngle + rotationSpeed/10}deg) scale(${currentScale/100})`;
        }, 50);
        isRotating = true;
        btn.textContent = '停止旋转';
        btn.classList.add('active');
    }
}

// 重置视角
function resetView() {
    const logo = document.getElementById('logo3d');
    logo.style.transform = 'rotateY(0deg) rotateX(0deg) rotateZ(0deg) scale(1)';
    currentScale = 100;
    document.getElementById('scaleSlider').value = 100;
    if (isRotating) {
        clearInterval(rotationInterval);
        isRotating = false;
        document.getElementById('rotationBtn').textContent = '开始旋转';
        document.getElementById('rotationBtn').classList.remove('active');
    }
}

// 切换粒子效果
function toggleParticles() {
    const particles = document.querySelectorAll('.particle');
    const btn = document.getElementById('particleBtn');
    particlesEnabled = !particlesEnabled;
    
    particles.forEach(particle => {
        particle.style.display = particlesEnabled ? 'block' : 'none';
    });
    
    if (particlesEnabled) {
        btn.textContent = '关闭粒子';
        btn.classList.add('active');
    } else {
        btn.textContent = '粒子效果';
        btn.classList.remove('active');
    }
}

// 更新旋转速度
function updateSpeed() {
    rotationSpeed = document.getElementById('speedSlider').value;
}

// 更新缩放
function updateScale() {
    currentScale = document.getElementById('scaleSlider').value;
    const logo = document.getElementById('logo3d');
    const currentTransform = logo.style.transform || '';
    const transformWithoutScale = currentTransform.replace(/scale\([^)]*\)/, '');
    logo.style.transform = transformWithoutScale + ` scale(${currentScale/100})`;
}

// 轴旋转函数
function rotateX() {
    const logo = document.getElementById('logo3d');
    const currentTransform = logo.style.transform || '';
    const rotation = currentTransform.match(/rotateX\(([^)]+)\)/) || [0, '0deg'];
    const currentAngle = parseInt(rotation[1]) || 0;
    const newTransform = currentTransform.replace(/rotateX\([^)]*\)/, '') + ` rotateX(${currentAngle + 90}deg)`;
    logo.style.transform = newTransform;
}

function rotateY() {
    const logo = document.getElementById('logo3d');
    const currentTransform = logo.style.transform || '';
    const rotation = currentTransform.match(/rotateY\(([^)]+)\)/) || [0, '0deg'];
    const currentAngle = parseInt(rotation[1]) || 0;
    const newTransform = currentTransform.replace(/rotateY\([^)]*\)/, '') + ` rotateY(${currentAngle + 90}deg)`;
    logo.style.transform = newTransform;
}

function rotateZ() {
    const logo = document.getElementById('logo3d');
    const currentTransform = logo.style.transform || '';
    const rotation = currentTransform.match(/rotateZ\(([^)]+)\)/) || [0, '0deg'];
    const currentAngle = parseInt(rotation[1]) || 0;
    const newTransform = currentTransform.replace(/rotateZ\([^)]*\)/, '') + ` rotateZ(${currentAngle + 90}deg)`;
    logo.style.transform = newTransform;
}

// 鼠标交互
document.getElementById('logo3d').addEventListener('mousemove', function(e) {
    if (!isRotating) {
        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = (y - centerY) / 15;
        const rotateY = (x - centerX) / 15;
        
        this.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(${currentScale/100})`;
    }
});

// 初始化
window.addEventListener('load', function() {
    createParticles();
    document.getElementById('particleBtn').textContent = '关闭粒子';
    document.getElementById('particleBtn').classList.add('active');
}); 