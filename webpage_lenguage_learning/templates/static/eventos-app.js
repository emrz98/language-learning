function oprimir(){
    reverso = document.getElementById("reverso").innerText;
    respuesta = document.getElementById("texto").value;
    blockRes = document.getElementById("resultado");
    if (reverso == respuesta){
        blockRes.style.backgroundColor = 'green';
        blockRes.innerText = "Correcto!";

    }
    else{
        blockRes.style.backgroundColor = 'red';
        blockRes.innerText = "Incorrecto";
    }
    document.getElementById("reverso").style.color = 'black';
}