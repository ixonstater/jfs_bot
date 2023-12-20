// https://ark.fandom.com/wiki/GFI_Codes

var tables = document.getElementsByClassName("wikitable")
var items = {}
for (let table of tables) {
    for (let tr of table.children[0].children) {
        if (tr.children[0].tagName == "TH") {
            // Header, continue
            continue
        }

        items.push({
            "displayName": tr.children[0].children[1].innerHTML,
            "gfiCommand": tr.children[1].children[0].children[0].innerHTML,
            "gfiCommandStack": tr.children[2].children[0].children[0].innerHTML,
        })
    }
}

console.log(JSON.stringify(items))