module.exports = {
    purge: {
        enabled: true,
        preserveHtmlElements: true,
        content: [
        './app/templates/**/*.html',
        ],
        theme: {
            extend: {},
        },
        plugins: [],
    },