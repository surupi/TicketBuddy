<template>
	<div>
		<b-navbar toggleable="xl" class="header">
			<b-navbar-brand>
				<router-link class="nav-heading" :to="{ path: '/' }">
					<div class="d-flex align-items-center">
						<img class="logo" src="../assets/logo.png" />
						TicketBuddy
					</div>
				</router-link>
			</b-navbar-brand>

			<b-navbar-toggle target="nav-collapse" />

			<b-collapse id="nav-collapse" is-nav>
				<b-navbar-nav class="ms-auto">
					<b-navbar-nav>
						<b-nav-item class="nav-flex-item">
							<router-link class="nav-item" :to="{ path: '/' }">
								Home
							</router-link>
						</b-nav-item>
						<span class="d-flex">
							<b-nav-item class="nav-flex-item">
								<router-link class="nav-item" :to="{ path: '/about' }">
									About
								</router-link>
							</b-nav-item>
							

							<span v-if="getSignedInState" style="display: flex">
								<span v-if="getUserType === 'customer'" style="display: flex">
									<b-nav-item class="nav-flex-item">
										<router-link class="nav-item" :to="{ path: '/pickvenue' }">
											Pick Venue
										</router-link>
									</b-nav-item>
									<b-nav-item class="nav-flex-item">
										<router-link class="nav-item" :to="{ path: '/profile' }">
											Profile
										</router-link>
									</b-nav-item>
								</span>

								<span v-if="getUserType === 'admin'" style="display: flex">
									<b-nav-item class="nav-flex-item">
										<router-link class="nav-item" :to="{ path: `/adminvenue` }">
											Venues
										</router-link>
									</b-nav-item>
									<b-nav-item class="nav-flex-item">
										<router-link class="nav-item" :to="{ path: `/admincategories` }">
											Categories
										</router-link>
									</b-nav-item>
									<b-nav-item class="nav-flex-item">
										<router-link class="nav-item" :to="{ path: `/adminbooking` }">
											Bookings
										</router-link>
									</b-nav-item>
									<b-nav-item class="nav-flex-item">
										<router-link class="nav-item" :to="{ path: `/admincustomers` }">
											Customers
										</router-link>
									</b-nav-item>
								</span>

								<b-nav-item class="nav-flex-item">
									<div class="logout" @click="signOut">Logout</div>
								</b-nav-item>
							</span>
							<span v-else style="display: flex">
								<b-nav-item class="nav-flex-item">
									<router-link class="nav-item" :to="{ path: '/register' }">
										Register
									</router-link>
								</b-nav-item>
								<b-nav-item class="nav-flex-item">
									<router-link class="nav-item" :to="{ path: '/login' }">
										Login
									</router-link>
								</b-nav-item>
							</span>
						</span>
					</b-navbar-nav>
				</b-navbar-nav>
			</b-collapse>
		</b-navbar>
	</div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
	name: 'Header',
	computed: {
		...mapGetters(['getSignedInState', 'getUserType', 'getCustID']),
	},
	methods: {
		...mapActions(['signOut']),
	},
};
</script>

<style scoped>
.logo {
	width: 40px;
	height: 35px;
	margin-right: 10px;
	margin-top: 3px;
}

@media (min-width: 768px) {
	.header {
		padding: 1rem 16rem;
	}
}

@media (max-width: 767px) {
	.header {
		padding: 1rem 2rem;
	}
}

@media (max-width: 600px) {
	.d-flex {
		display: block !important;
	}
}

.nav-heading {
	color: #000 !important;
	text-decoration: none !important;
	display: flex;
	flex-direction: row;
	align-items: center;
	font-weight: 600;
	font-size: 20px;
}

.nav-item {
	padding: 0 4px !important;
	font-size: 18px;
	color: #000;
	font-weight: 600;
	text-decoration: none !important;
}

.logout {
	color: #000;
}
</style>
