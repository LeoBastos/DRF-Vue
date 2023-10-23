<template>
    <header class="text-gray-600 body-font dark:bg-gray-700">
        <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">           
            <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
                 <RouterLink to="/product" class="mr-5 hover:text-emerald-500 dark:text-white">Produtos</RouterLink>
                 <RouterLink to="/suplier" class="mr-5 hover:text-emerald-500 dark:text-white">Fornecedores</RouterLink>
                 <RouterLink to="/category" class="mr-5 hover:text-emerald-500 dark:text-white">Categorias</RouterLink>
              
            </nav>
            <RouterLink to="/login" class="mr-5 hover:text-emerald-500 dark:text-white">Login</RouterLink>
    </div>
</header></template>