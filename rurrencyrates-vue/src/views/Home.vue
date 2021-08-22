<template>
  <div class="home">
    <section class="">
      <div class="has-text-centered">
        <p class="title">Currencies:</p>
      </div>
    </section>
    <div class="columns is-mulytyline">
      <div 
        class="column is-2" 
        v-for="currency in currencylist"
        :key="currency.id"
        @click="selectCurrency(currency)"
      >
        <div 
          :class="selectedcurrency == currency ? 'is-primary' : ''"
          class="box hero has-text-centered mb-6">
          <h3 class="is-size-3">{{ currency.name }}</h3>
          <button class="button">del</button>
        </div>
      </div>
    </div>
    <div v-if="selectedcurrency">
      <div 
        class="columns is-mulytyline"
        v-for="rate in selectedrates"
        :key="rate.id"
      >
        <h3 class="column is-2">{{ rate.date }} | {{ rate.rate }}</h3>
      </div>
      <input 
        v-model="date"
        type="text"
        class="input"
        style="width: 15%"
      >
      <input 
        v-model="rate"
        type="text"
        class="input"
        style="width: 15%"
      >
      <button 
      @click="addRate"
      class="button">
      Add
    </button>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Home',

    data() {
      return {
        currencylist: [],
        rateslist: [],
        selectedcurrency: null,
        selectedrates: [],
        date: null,
        rate: null,
      }
    },

    components: {
    },

    mounted() {
      this.getCurrencyList()
      this.getRatesList()
    },

    methods: {
      getCurrencyList() {
        axios
          .get('/api/v1/currencies/')
          .then(response => {
            this.currencylist = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },

      getRatesList() {
        axios
          .get('/api/v1/rates/')
          .then(response => {
            this.rateslist = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },

      selectCurrency(cur) {
        this.selectedcurrency = cur
        this.selectedrates = []
        this.rateslist.forEach(rate => {
          if (rate.currency == cur.id) {
            this.selectedrates.push(rate)
          }
        });
      },

      addRate() {
        const rate = {
          currency: this.selectedcurrency,
          date: this.date,
          rate: this.rate
        }
        axios
          .post('/api/v1/rates/', rate)
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
      },
    }
  }
</script>
