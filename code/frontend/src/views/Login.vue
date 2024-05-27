<template>
    <div class="login">
        <div class="login-form">
            <div class="login-form-header">Welcome back! Please login!</div>
            <div class="login-form-body">
                <validation-observer v-slot="{ invalid, handleSubmit }">
                    <form @submit.prevent="handleSubmit(login)">
                        <div class="form-group">
                            <label for="email">Email</label>
                            <validation-provider
                                rules="required|email|max:30"
                                v-slot="{ errors }"
                            >
                                <input
                                    type="email"
                                    id="email"
                                    v-model="email"
                                    placeholder="Enter your email"
                                />
                                <div class="text-danger push-right">
                                    {{ errors[0] }}
                                </div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="password">Password</label>
                            <validation-provider
                                rules="required|min:6|max:30"
                                v-slot="{ errors }"
                            >
                                <input
                                    type="password"
                                    id="password"
                                    v-model="password"
                                    placeholder="Enter your password"
                                />
                                <div class="text-danger push-right">
                                    {{ errors[0] }}
                                </div>
                            </validation-provider>
                        </div>
                        <b-button
                            @click="show = true"
                            type="submit"
                            class="btn-bg btn-yellow push-right"
                            :disabled="invalid"
                        >
                            Login
                        </b-button>
                        <div class="bottom-question">
                            <router-link class="router-link" to="/adminlogin">
                                Are you an admin? Please login here
                            </router-link>
                        </div>

                        <b-modal
                            v-model="show"
                            id="login"
                            type="submit"
                            :title="loginFormHeader"
                        >
                            <p class="my-4">{{ loginFormText }}</p>
                            <template #modal-footer>
                                <b-button
                                    size="md"
                                    class="float-right btn-yellow"
                                    @click="routehomePage()"
                                >
                                    OK
                                </b-button>
                            </template>
                        </b-modal>
                    </form>
                </validation-observer>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions } from "vuex";
import { ValidationProvider, ValidationObserver } from "vee-validate";

export default {
    name: "Login",
    data() {
        return {
            email: "",
            password: "",
            loginFormHeader: "Confirming User Credentials",
            loginFormText:
                "Please wait while we are verifying your information",
            shouldRoute: false,
            show: false,
        };
    },
    components: {
        ValidationObserver,
        ValidationProvider,
    },
    methods: {
        ...mapActions(["loginUser"]),
        routehomePage() {
            this.show = false;
            if (this.shouldRoute) this.$router.push("/");
        },
        login() {
            this.loginUser({
                email: this.email,
                password: this.password,
            })
                .then(() => {
                    // if the user is not logged in already, it means that the login has failed
                    if (this.$store.getters.getSignedInState) {
                        this.loginFormHeader = "Success!";
                        this.loginFormText = "Succesfully logged in!";
                        this.shouldRoute = true;
                    }
                    // error case
                    else {
                        this.loginFormHeader = "Error!";
                        this.loginFormText = "Invalid User Credentials!";
                    }
                })
                .catch(() => {
                    this.loginFormHeader = "Error!";
                    this.loginFormText = "Something went wrong!";
                });
        },
    },
};
</script>

<style scoped>
.login {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 50px 0 100px 0;
}
.login-form {
    background-color: #f5f5f5;
    padding: 50px 200px;
}
.login-form-header {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 50px;
    text-align: center;
}
.login-form-error {
    padding: 10px 0;
    color: #fff;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 50px;
    text-align: center;
}
label {
    width: 150px;
    font-weight: 500;
}
.form-group {
    margin-bottom: 30px;
}
input {
    width: 400px;
    height: 35px;
    border: 1px solid #eee;
    padding: 0 10px;
}
textarea {
    width: 600px;
    height: 100px;
    border: 1px solid #eee;
    padding: 10px;
    resize: none;
}
.textarea-label {
    vertical-align: top;
}
.btn-yellow {
    background-color: #e4c314 !important;
    color: #000 !important;
    margin-left: 150px;
    font-weight: 600;
}
.btn-yellow:disabled {
    background-color: #666 !important;
    color: #fff !important;
}
.bottom-question {
    padding-top: 27px;
    margin-left: 150px;
}
.push-right {
    margin-left: 150px;
}
</style>
