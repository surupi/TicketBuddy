import Vue from 'vue';
import App from './App.vue';
import router from './router';
import bootstrap from './plugins/bootstrap';
import store from './store';
import './plugins/validation';


//configures the Vue.js application's production tip,
// creates a Vue instance,
// sets up routing,
// Bootstrap-related setup,
// connects the Vuex store,
// specifies how the root component should be rendered,
// and finally mounts the Vue instance

Vue.config.productionTip = false;
new Vue({
	router,
	bootstrap,
	store,
	render: (h) => h(App),
}).$mount('#app');