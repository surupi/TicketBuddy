<template>
	<div class="home">
		<div class="banner-container">
			<img class="banner" src="../assets/home-banner.jpg" alt="home-banner" />
			<div class="banner-text">
				<div class="heading">Welcome to TicketBuddy!</div>
				<div class="text">
					Looking to book a movie?<br>
					Look no further! Here at TicketBuddy, we will help you to book the latest blockbusters with ease.<br><br>
					Enter the world of cinematic delight, with curated collection of the latest movies and showtimes, right at your fingertips.
					Our platform is your gateway to hassle-free ticket booking experience.<br>
				</div>
				<div class="button">
					<router-link class="button-text" to="/about"><b>Learn more about us!</b></router-link>
				</div>
			</div>
		</div>

		<div class="outer-services">
			<div class="container" style="textalign: center">
				<div class="section-heading">Plan your next movie outing with us</div>
				<div class="services">
					<div class="service">
						<img src="../assets/home-icons/fast.png" alt="fast" />
						<div class="service-heading">Fast ticket booking experience</div>
					</div>
					<div class="service">
						<img src="../assets/home-icons/movie.png" alt="movie" />
						<div class="service-heading">Plethora of movies to choose from</div>
					</div>
					<div class="service">
						<img src="../assets/home-icons/calender.png" alt="calender" />
						<div class="service-heading">Timely remainders</div>
					</div>
					<div class="service">
						<img src="../assets/home-icons/user.png" alt="user" />
						<div class="service-heading">User friendly interface</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Home',
};
</script>

<style scoped>
.banner-container {
	position: relative;
}

.banner {
	width:100%;
	height:50%;
}

.banner-text {
	position: absolute;
	top: 30%;
	left: 20%;
	width: 600px;
}

.heading {
	font-size: 3rem;
	font-weight: bold;
	color: #fff;
}

.button {
	background-color: #e4c314;
	width: 200px;
	padding: 6px 10px;
	margin-top: 20px;
	display: flex;
	align-items: center;
	justify-content: center;
}

.button:hover {
	cursor: pointer;
}

.text {
	width: 400px;
	font-size: 1.1rem;
	color: #eee;
	margin-top: 10px;
}

.button-text {
	font-size: 1.1rem;
	color: #000;
	text-decoration: none;
}

.outer-services {
	background-color: #f5f5f5;
	padding: 60px 0 80px 0;
}

.services {
	display: flex;
	flex-wrap: wrap;
	justify-content: space-around;
}

.service {
	width: 280px;
	height: 300px;
	padding: 20px 40px;
	background-color: #fff;
	box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
}

.service-heading {
	font-size: 1.25rem;
	font-weight: bold;
	color: #000;
	padding-top: 20px;
	padding-bottom: 10px;
}

.service-text {
	color: #000;
}

.who-are-we {
	padding: 80px 0;
	text-align: center;
}

.section-heading {
	font-size: 2.2rem;
	font-weight: bold;
	color: #000;
	padding-bottom: 30px;
	text-align: center;
}

.section-text {
	font-size: 1.1rem;
	color: #000;
}
</style>
