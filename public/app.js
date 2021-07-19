


var myapp=new Vue({
    data () {
      return {
          baseUrl: 'api:5000', // API url
          searchTerm: 'Hello World', // Default search term
          searchDebounce: null, // Timeout for search bar debounce
          searchResults: [], // Displayed search results
          numHits: null, // Total search results found
          searchOffset: 0, // Search result pagination offset
  
          resultTitle:'',
          resultBody:'',
          tags:[]
      }
    },
    async created () {
      this.searchResults = await this.search() // Search for default term
    },

    /** Trucate the result body to 200 words */

    filters: {
      truncate: function (text, length, suffix) {
          if (text.length > length) {
              return text.substring(0, length) + suffix;
          } else {
              return text;
          }
      },
  },
    methods:{
  
      onSearchInput () {

        clearTimeout(this.searchDebounce)
        this.searchDebounce = setTimeout(async () => {
          this.searchOffset = 0
          this.searchResults = await this.search()
        },100)
      },
  
       /** Call API to search for inputted term */
  
      async search () {

        const response = await axios.get(`${this.baseUrl}/search`, { params: { term: this.searchTerm, offset: this.searchOffset } })

        this.numHits = response.data.hits.total.value

        console.log(response.data.hits.total.value);
        const path=response.data.hits.hits[0]._source
        console.log(response.data.hits.hits[0]._source.title);
        console.log(response.data.hits.hits[0]._source.body);
        console.log(response.data.hits.hits[0]._source.tag);
        const t=path.tag
        var tempTag=t.replace(/[\[\]']+/g, '');
        console.log(tempTag);
        tempTag=tempTag.split(',');
        console.log(tempTag);

        this.resultTitle=path.title
        this.resultBody=path.body
        this.tags=tempTag


        return response.data.hits.hits
      },

      /** Get next page of search results */
    async nextResultsPage () {

      if (this.numHits > 10) {
        this.searchOffset += 10
        if (this.searchOffset + 10 > this.numHits) { this.searchOffset = this.numHits - 10}
        this.searchResults = await this.search()
        document.documentElement.scrollTop = 0
      }

    },
    /** Get previous page of search results */
    async prevResultsPage () {

      this.searchOffset -= 10
      if (this.searchOffset < 0) { this.searchOffset = 0 }
      this.searchResults = await this.search()
      document.documentElement.scrollTop = 0
      
    }


  
    }
  
}).$mount('#app')
