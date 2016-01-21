function dogYears (humanYears) {
    return humanYears * 7;
}

if (typeof require !== 'undefined' && require.main === module) {
    console.log('4 human years gives dog years of', dogYears((4)));
}
