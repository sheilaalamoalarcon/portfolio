function goUp () {
    var top = document.getElementById('top');
    console.log('top');
    return top.scrollIntoView({behavior: 'smooth'});
}
function showSketchModal () {
    var modal = document.getElementById('sketchModal');
    const getSketchName = document.getElementById('sketchName');
    modal.style.display = 'block';
}