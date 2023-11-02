# FSI-Branch-And-Bound

Al comenzar la práctica, empezamos con el fichero ["run.py"](run.py), que se trata de unos tests manuales. Por tanto, creamos la función para mostrar los resultados de diferentes algoritmos de búsqueda que puede ser la búsqueda en amplitud, en profundidad, ramificación y acotación, y ramificación y acotación con subestimación. Hemos utilizado el uso de la llamada de esta función para permitir que buscara una ruta diferente para poder mostrar información detallada con los diferentes algoritmos de búsqueda.

Por un lado, hemos añadido un fichero ["test_search.py"](test_search.py), que vamos a usar el test automatizado para poder comprobar si los resultados están correctos. Por otro lado, pasamos a otro fichero ["search.py"](search.py), hemos modificado el código donde se realiza la búsqueda de un grafo para poder encontrar la solución a un problema dado, registrando información sobre el progreso de la búsqueda, es decir, obtenemos los números de nodos generados y visitados, el tiempo de ejecución y el costo total de la solución. Después de todo, hemos implementado varias funciones de cada algoritmos de búsqueda.

A continuación, pasamos con el último fichero ["utils.py"](utils.py), hemos definido tres clases que se utilizan en algoritmos de búsqueda, y todas heredan de una clase denominada Queue.

Por tanto, la primera clase "FIFOQueue", es el encargado de implementar una cola en la que los elementos se manejan de manera FIFO, es decir, "primero en entrar, primero en salir".

La segunda clase "BranchAndBound", se encarga de administrar una lista de nodos utilizado el algoritmo de Ramificación y Acotación, que explora asegurándose de que los nodos se examinen en orden de costo ascendente y vaciando la lista para evitar el exceso de nodos.

Por último, con la última clase "BranchAndBound_with_heuristics", se aplica el mismo algoritmo de búsqueda de Ramificación y Acotación, pero esta vez, se considera que se usa la heurística para poder guiar la exploración hacia soluciones posiblemente mejores. Teniendo en cuenta, que la heurística viene de un algoritmo de búsqueda informada que se usa una función para aplicar la suma entre el costo total y la heurística, donde viene la distancia mínima entre los grafos o ciudades en el mapa de Rumania.
