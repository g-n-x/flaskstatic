var count = 0;
function addResposta() {
    count += 1;
    var cont = `
        <div id='div${count}' class="center-container" style='padding:5px;'>
        Questão ${count} | 
            Resposta:
            <select style='margin: 0 20px 0 2px' name="cars" id="cars">
                <option value="correto">Correto</option>
                <option value="errado">Errado</option>
            </select>
            Peso:
            <input style='margin: 0 20px 0 2px; width: 40px' type='number' value=1 placeholder='Valor do peso' min=1>
        </div>
    `;
    document.getElementById("add_resposta").innerHTML += cont;
}

function removeResposta() {
    if(count >= 1) {
        document.getElementById(`div${count}`).remove();
        count -= 1;
        console.log(count)
    }
}
