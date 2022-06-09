const { createApp } = Vue

createApp({
    mounted() {
        fetch('./scenarios.json')
            .then(response => response.json())
            .then(scenarios => {
                this.scenarios = scenarios
            })
    },
    methods: {
        makeDecision(choice) {
            this.currentChoiceName = choice
        },
        goToNextScenario(scenarioName) {
            this.currentScenarioName = scenarioName
            this.currentChoiceName = ''
        }
    },
    computed: {
        currentScenario() {
            return this.scenarios[this.currentScenarioName]
        },
        currentChoice() {
            return this.currentScenario?.choices?.find(({ choice }) => choice === this.currentChoiceName)
        }
    },
    data() {
        return {
            message: 'Hello Vue!',
            currentScenarioName: 'start',
            currentChoiceName: '',
            scenarios: {},
        }
    },
}).mount('#app')