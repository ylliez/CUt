const totalSlices = 8;

for (let i = 1; i <= totalSlices; i++) {
    const unlocked = localStorage.getItem(`slice${i}`);
    const cell = document.getElementById(`slice${i}`);

    if (unlocked === 'true') {
        cell.style.backgroundImage = `url('slices/slice_${i}.png')`;
    } else {
        cell.style.backgroundColor = '#999';
    }
}

document.getElementById('resetBtn').addEventListener('click', () => {
    for (let i = 1; i <= totalSlices; i++) {
        localStorage.removeItem(`slice${i}`);
    }
    location.reload();
}); s