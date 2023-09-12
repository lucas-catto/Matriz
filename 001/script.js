function division(matriz_00, matriz_01) {
    
    if (matriz_00.length !== matriz_01.length) {
        throw new Error("As matrizes devem ter o mesmo tamanho.");
    }
    
    const result = [];

    for (let i = 0; i < matriz_00.length; i++) {
        result.push([])
        for (let j = 0; j < matriz_01.length; j++) {
            result[i].push(matriz_00[i][j] / matriz_01[i][j]);
        }
        return result;
    }
}

const matriz_00 = [[1,2], [3,4]];
const matriz_01 = [[5,6], [7,8]];

const resultMatriz = division(matriz_00, matriz_01);

console.table(resultMatriz)
