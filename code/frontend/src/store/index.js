import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../router';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		isSignedIn: false,
		user: {},
		categories: [],
		category: {},
		booking: [],
		venue: [],
		movie: [],
		userType: '',
	},
	getters: {
		getSignedInState: (state) => state.isSignedIn,
		getUserType: (state) => state.userType,
		getUser: (state) => state.user,
		getCategories: (state) => state.categories,
		getCategory: (state) => state.category,
		getCustID: (state) => state.user.cust_id,
		getAdminID: (state) => state.user.admin_id,
		getBooking: (state) =>state.booking,
		getVenue: (state) => state.venue,
		getMovie: (state) => state.movie,
		getAccessToken: (state) => state.user.access_token,
	},
	mutations: {
		loginUser: (state, user) => {
			state.user = user;
			state.userType = 'customer';
			state.isSignedIn = true;
		},
		loginAdmin: (state, admin) => {
			state.user = admin;
			state.userType = 'admin';
			state.isSignedIn = true;
		},
		signOut: (state) => {
			state.user = {};
			state.movie = {};
			state.isSignedIn = false;
			state.userType = '';
			router.push('/login');
		},
		setMovie: (state, payload) => {
			state.movie = [...payload];
		},
		setCategories: (state, payload) => {
			state.categories = [...payload];
		},
		setBooking: (state, payload) => {
			state.booking = payload;
		},
		setVenue: (state, payload) => {
			state.venue = payload;
		},
		routeModifyCategory: (state, payload) => {
			state.category = payload;
		},
		routeModifyVenue: (state, payload) => {
			state.venue = payload;
		},
		routeModifyMovie: (state, payload) => {
			state.movie = payload;
		},
		routeModifyBooking: (state, payload) => {
			state.booking = payload;
		},
	},
	actions: {
		signOut({ commit }) {
			commit('signOut');
		},
		routeModifyMovie({ commit }, payload) {
			commit('routeModifyMovie', payload);
		},

		routeModifyCategory({ commit }, payload) {
			commit('routeModifyCategory', payload);
		},

		routeModifyVenue({ commit }, payload) {
			commit('routeModifyVenue', payload);
		},
		
		async registerUser(_, account) {
			await axios
				.post('http://localhost:5000/register', account, {
					headers: {'Content-Type': 'application/json',
					},
				})
				.then((response) => {
					if (!response.data.error) {
						router.push({ name: 'Login' });
					}
				});
		},

		async loginUser({ commit}, account) {
			await axios
				.post('http://localhost:5000/login', account, {
					headers: {
						'Content-Type': 'application/json'
					},
				})
				.then((response) => {
					// if the server does not respond with the error object, it means that the user can be authenticated
					if (!response.data.error) {
						const token = response.data.access_token;
						localStorage.setItem('token', token);
						commit('loginUser', response.data);
					}
				});
		},

		async loginAdmin({ commit}, account) {
			await axios
				.post('http://localhost:5000/loginadmin', account, {
					headers: {
						'Content-Type': 'application/json'
					},
				})
				.then(async (response) => {
					if (!response.data.error) {
						const token = response.data.access_token;
						localStorage.setItem('token', token);
						commit('loginAdmin', response.data);
						router.push('/')
					}
				});
		},

		async loadMovie({ commit, state }) {
			await axios
				.get('http://localhost:5000/adminmovie', {
					headers: {"Content-Type":"application/json",
					Authorization: `Bearer ${state["user"]["access_token"]
				}`}})
				.then((response) => {
					commit('setMovie', response.data);
				});
		},

		async loadCategories({ commit, state }) {
			await axios
				.get('http://localhost:5000/admincategories', {
					headers: {"Content-Type":"application/json",
					Authorization: `Bearer ${state["user"]["access_token"]
				}`}}
				)
				.then((response) => {
					commit('setCategories', response.data);
				});
		},

		async loadVenue({ commit, state }) {
			await axios
				.get('http://localhost:5000/adminvenue', {
					headers: {"Content-Type":"application/json",
					Authorization: `Bearer ${state["user"]["access_token"]
				}`}})
				.then((response) => {
					commit('setVenue', response.data);
				});
		},

		async loadBooking({ commit, state }) {
			await axios
				.get('http://localhost:5000/useaddbooking', {
					headers: {"Content-Type":"application/json",
					Authorization: `Bearer ${state["user"]["access_token"]
				}`}})
				.then((response) => {
					commit('setBooking', response.data);
				});
		},

		async updateProfile(_, account) {
			await axios.put('http://localhost:5000/updateprofile', account, {
				headers: {
					'Content-Type': 'application/json',
				},
			});
		},
	},
});
