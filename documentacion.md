# Documentación de la API

## URL Base

Todas las rutas siguientes asumen la URL base es `/`.

---

### Rutas de Productos

#### Obtener Todos los Productos

**URL:** `/productos`  
**Método:** `GET`  
**Descripción:** Recuperar todos los productos.

**Respuestas:**

- `200 OK` - Devuelve una página HTML renderizada con la lista de productos.

#### Obtener Producto por ID

**URL:** `/productos/id/<id>`  
**Método:** `GET`  
**Descripción:** Recuperar un producto por su ID.

**Parámetros:**

- `id` (int): El ID del producto.

**Respuestas:**

- `200 OK` - Devuelve los detalles del producto en JSON.
- `404 Not Found` - Si el producto no se encuentra.

#### Obtener Producto por Nombre

**URL:** `/productos/nombre/<nombre>`  
**Método:** `GET`  
**Descripción:** Recuperar un producto por su nombre.

**Parámetros:**

- `nombre` (str): El nombre del producto.

**Respuestas:**

- `200 OK` - Devuelve los detalles del producto en JSON.
- `404 Not Found` - Si el producto no se encuentra.

#### Obtener Calorías del Producto por ID

**URL:** `/productos/calorias/<id>`  
**Método:** `GET`  
**Descripción:** Recuperar las calorías totales de un producto por su ID.

**Parámetros:**

- `id` (int): El ID del producto.

**Respuestas:**

- `200 OK` - Devuelve el ID del producto y las calorías totales en JSON.
- `404 Not Found` - Si el producto no se encuentra.

#### Obtener Rentabilidad del Producto por ID

**URL:** `/productos/rentabilidad/<id>`  
**Método:** `GET`  
**Descripción:** Recuperar la rentabilidad de un producto por su ID.

**Parámetros:**

- `id` (int): El ID del producto.

**Respuestas:**

- `200 OK` - Devuelve el ID del producto y la rentabilidad en JSON.
- `404 Not Found` - Si el producto no se encuentra.

#### Obtener Costo del Producto por ID

**URL:** `/productos/costo/<int:id>`  
**Método:** `GET`  
**Descripción:** Recuperar el costo de un producto por su ID.

**Parámetros:**

- `id` (int): El ID del producto.

**Respuestas:**

- `200 OK` - Devuelve el ID del producto y el costo en JSON.
- `404 Not Found` - Si el producto no se encuentra.

#### Vender Producto por ID

**URL:** `/ventas/id/<int:id>`  
**Método:** `GET`, `POST`  
**Descripción:** Vender un producto por su ID.

**Parámetros:**

- `id` (int): El ID del producto.

**Respuestas:**

- `200 OK` - Si la venta fue exitosa.
- `400 Bad Request` - Si no hay suficiente inventario de ingredientes.
- `404 Not Found` - Si el producto no se encuentra.

---

### Rutas de Ingredientes

#### Obtener Todos los Ingredientes

**URL:** `/ingredientes`  
**Método:** `GET`  
**Descripción:** Recuperar todos los ingredientes.

**Respuestas:**

- `200 OK` - Devuelve una página HTML renderizada con la lista de ingredientes.

#### Obtener Ingrediente por ID

**URL:** `/ingredientes/id/<int:id>`  
**Método:** `GET`  
**Descripción:** Recuperar un ingrediente por su ID.

**Parámetros:**

- `id` (int): El ID del ingrediente.

**Respuestas:**

- `200 OK` - Devuelve los detalles del ingrediente en JSON.
- `404 Not Found` - Si el ingrediente no se encuentra.

#### Obtener Ingrediente por Nombre

**URL:** `/ingredientes/nombre/<nombre>`  
**Método:** `GET`  
**Descripción:** Recuperar un ingrediente por su nombre.

**Parámetros:**

- `nombre` (str): El nombre del ingrediente.

**Respuestas:**

- `200 OK` - Devuelve los detalles del ingrediente en JSON.
- `404 Not Found` - Si el ingrediente no se encuentra.

#### Verificar si un Ingrediente es Sano por ID

**URL:** `/ingredientes/essano/<int:id>`  
**Método:** `GET`  
**Descripción:** Verificar si un ingrediente es sano por su ID.

**Parámetros:**

- `id` (int): El ID del ingrediente.

**Respuestas:**

- `200 OK` - Devuelve el ID del ingrediente, su nombre y si es sano en JSON.
- `404 Not Found` - Si el ingrediente no se encuentra.

#### Abastecer Ingrediente por ID

**URL:** `/ingredientes/abastecer/<int:id>`  
**Método:** `GET`, `POST`  
**Descripción:** Abastecer el inventario de un ingrediente por su ID.

**Parámetros:**

- `id` (int): El ID del ingrediente.

**Respuestas:**

- `200 OK` - Devuelve un mensaje de éxito.
- `404 Not Found` - Si el ingrediente no se encuentra.

#### Renovar Inventario de Ingrediente por ID

**URL:** `/ingredientes/renovar-inventario/<int:id>`  
**Método:** `GET`, `POST`  
**Descripción:** Renovar el inventario de un ingrediente por su ID.

**Parámetros:**

- `id` (int): El ID del ingrediente.

**Respuestas:**

- `200 OK` - Devuelve un mensaje de éxito.
- `404 Not Found` - Si el ingrediente no se encuentra.
