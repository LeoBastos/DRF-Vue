import { defineStore } from 'pinia';

export const useAlertStore = defineStore({
  id: 'alert',
  state: () => ({
    message: '',
    type: '',
  }),
  actions: {
    showAlert(message, type) {
      this.message = message;
      this.type = type;

      setTimeout(() => {
        this.clearAlert();        
      }, 3000);
    },
    clearAlert() {
      this.message = '';
      this.type = '';   
    },
  },
});