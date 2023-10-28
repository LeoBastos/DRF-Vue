<template>
    <div class="flex items-center justify-between mt-6">
        <div>
            <a href="#" @click="loadPreviousPage" v-if="previous"
                class="flex items-center px-5 py-2 text-sm text-gray-700 capitalize transition-colors duration-200 bg-white border rounded-md gap-x-2 hover:bg-gray-100 dark:bg-gray-900 dark:text-gray-200 dark:border-gray-700 dark:hover:bg-gray-800">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-5 h-5 rtl:-scale-x-100">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 15.75L3 12m0 0l3.75-3.75M3 12h18" />
                </svg>

                <span>
                    Anterior
                </span>
            </a>
        </div>

        <div class="items-center hidden md:flex gap-x-3">
            <button v-for="page_num in totalPages" :key="page_num"
                :class="['px-2 py-1 text-sm rounded-md', currentPage === page_num ? 'active text-blue-500 dark:bg-gray-800 bg-blue-100/60' : 'text-gray-500 dark:hover:bg-gray-800 dark:text-gray-300 hover:bg-gray-100']"
                @click.prevent="changePage(page_num)">
                {{ page_num }}
            </button>
        </div>
        <div>
            <a href="#" @click="loadNextPage" v-if="next"
                class="flex items-center px-5 py-2 text-sm text-gray-700 capitalize transition-colors duration-200 bg-white border rounded-md gap-x-2 hover:bg-gray-100 dark:bg-gray-900 dark:text-gray-200 dark:border-gray-700 dark:hover:bg-gray-800">
                <span>
                    Próximo
                </span>

                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-5 h-5 rtl:-scale-x-100">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25L21 12m0 0l-3.75 3.75M21 12H3" />
                </svg>
            </a>
        </div>

    </div>
</template>


<script>
export default {
    props: ['currentPage', 'totalPages', 'next', 'previous'],
    methods: {
        changePage(page) {
            this.$emit('change-page', page);
        },
        loadNextPage() {
            if (this.next) {
                this.changePage(this.currentPage + 1);
            }
        },
        loadPreviousPage() {
            if (this.previous) {
                this.changePage(this.currentPage - 1);
            }
        }
    }
}
</script>