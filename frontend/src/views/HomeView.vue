<script setup>

</script>

<template>
  <section class="max-w-4xl  p-6 mt-6 mx-auto bg-white rounded-md shadow-md dark:bg-gray-800">
        <h2 class="text-lg font-medium text-gray-800 dark:text-white text-center">Bem vindo</h2>
        <h6 class="text-center text-sm font-small text-gray-800 dark:text-white">Faça login para acessar</h6>
        <div class="mt-6 md:flex md:items-center md:justify-center">
            <RouterLink to="/login" class=" modal-default-button px-8 py-2.5 leading-5 text-sm text-gray-800 transition-colors duration-200  border rounded-lg sm:w-auto dark:hover:bg-gray-600  hover:bg-gray-100 dark:text-white dark:border-gray-700">Login</RouterLink>
        </div>
    </section>
    
</template>
