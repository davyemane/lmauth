function displayConjug() {
    let element1=document.getElementById('block-conjug1')
    let element2=document.getElementById('block-conjug2')
    let element3=document.getElementById('block-conjug3')

    let element4=document.getElementById('joy-verbe')
    let element5=document.getElementById('consigne-voir-conjug')

    // pour la ligne info dans le modal de l'expert voir conjugaison
    let element6=document.getElementById('row-info')
    element1.style.display='block'
    element2.style.display='block'
    element3.style.display='block'

    element4.style.display='none'
    element5.style.display='none'

    element6.style.display='block'
}
