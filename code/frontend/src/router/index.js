import Vue from 'vue';
import VueRouter from 'vue-router';

// Common routes
import Home from '../views/Home.vue';
import About from '../views/About.vue';

// User routes
import Register from '../views/Register.vue';
import Login from '../views/Login.vue';
import Profile from '../views/Profile.vue';
import PickVenue from '../views/PickVenue.vue';
import PickMovie from '../views/PickMovie.vue';


// Admin routes
import AdminLogin from '../views/AdminLogin.vue';
import AdminCustomers from '../views/AdminCustomers.vue';
import AdminCategories from '../views/AdminCategories.vue';
import AdminAddCategory from '../views/AdminAddCategory.vue';
import AdminModifyCategory from '../views/AdminModifyCategory.vue';
import AdminVenue from '../views/AdminVenue.vue';
import AdminAddVenue from '../views/AdminAddVenue.vue';
import AdminModifyVenue from '../views/AdminModifyVenue.vue';
import AdminMovie from '../views/AdminMovie.vue';
import AdminAddMovie from '../views/AdminAddMovie.vue';
import AdminModifyMovie from '../views/AdminModifyMovie.vue';
import UserAddBooking from '../views/UserAddBooking.vue';
import Export from '../views/Export';
import AdminBooking from '../views/AdminBooking.vue';


Vue.use(VueRouter);

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home,
	},
	{
		path: '/about',
		name: 'About',
		component: About,
	},
	{
		path: '/profile',
		name: 'Profile',
		component: Profile,
	},
	{
		path: '/register',
		name: 'Register',
		component: Register,
	},
	{
		path: '/login',
		name: 'Login',
		component: Login,
	},
	{
		path: '/adminlogin',
		name: 'AdminLogin',
		component: AdminLogin,
	},
	{
		path: '/admincustomers',
		name: 'AdminCustomers',
		component: AdminCustomers,
	},
	{
		path: '/admincategories',
		name: 'AdminCategories',
		component: AdminCategories,
	},
	{
		path: '/adminaddcategory',
		name: 'AdminAddCategory',
		component: AdminAddCategory,
	},
	{
		path: '/adminmodifycategory/:category_id',
		name: 'AdminModifyCategory',
		component: AdminModifyCategory,
	},
	{
		path: '/adminvenue',
		name: 'AdminVenue',
		component: AdminVenue,
		props: true
	},
	{
		path: '/adminaddvenue',
		name: 'AdminAddVenue',
		component: AdminAddVenue,
	},
	{
		path: '/adminmodifyvenue/:venue_id',
		name: 'AdminModifyVenue',
		component: AdminModifyVenue,
		props: true
	},
	{
		path: '/adminmovie/:venue_id',
		name: 'AdminMovie',
		component: AdminMovie,
		props: true,
	},
	{
		path: '/adminaddmovie/:venue_id',
		name: 'AdminAddMovie',
		component: AdminAddMovie,
		props: true,
	},
	{
		path: '/adminmodifymovie/:movie_id',
		name: 'AdminModifyMovie',
		component: AdminModifyMovie,
		props: true
	},
	{
		path: '/pickvenue',
		name: 'PickVenue',
		component: PickVenue,
	},
	{
		path: '/pickmovie/:venue_id',
		name: 'PickMovie',
		component: PickMovie,
		props: true
	},
	{
		path: '/useraddbooking/:movie_id',
		name: 'UserAddBooking',
		component: UserAddBooking,
		props: true
	},
	{
		path: '/adminbooking',
		name: 'AdminBooking',
		component: AdminBooking,
	},
	{
        path:'/export',
        name:'Export',
        component:Export
    },
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});
export default router;
