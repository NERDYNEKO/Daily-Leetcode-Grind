class Solution:
    def toLowerCase(self, s: str) -> str:
        output=""
        prev = {
    "A":"a", "B":"b", "C":"c", "D":"d", "E":"e",
    "F":"f", "G":"g", "H":"h", "I":"i", "J":"j",
    "K":"k", "L":"l", "M":"m", "N":"n", "O":"o",
    "P":"p", "Q":"q", "R":"r", "S":"s", "T":"t",
    "U":"u", "V":"v", "W":"w", "X":"x", "Y":"y",
    "Z":"z"
}
        for i in s:
            if i in prev:
                i=prev[i]
            else:
                pass
            output+=i
        return output
                
