<!DOCTYPE html>
<html lang="zh-Hant">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>AI Todo Assistant</title>

<style>
body{
    font-family: "Microsoft JhengHei",sans-serif;
    background:#f4f7fb;
    margin:0;
}

.header{
    background:linear-gradient(135deg,#4f46e5,#06b6d4);
    color:white;
    text-align:center;
    padding:50px;
}

.container{
    max-width:900px;
    margin:auto;
    padding:20px;
}

.card{
    background:white;
    border-radius:15px;
    padding:25px;
    margin-bottom:20px;
    box-shadow:0 3px 10px rgba(0,0,0,.1);
}

h2{
    color:#4f46e5;
}

pre{
    background:#1e293b;
    color:#22c55e;
    padding:15px;
    border-radius:10px;
}

input{
    width:70%;
    padding:12px;
    border:1px solid #ccc;
    border-radius:8px;
}

button{
    padding:12px 18px;
    border:none;
    border-radius:8px;
    background:#4f46e5;
    color:white;
    cursor:pointer;
}

button:hover{
    background:#3730a3;
}

li{
    background:#f8fafc;
    margin:10px 0;
    padding:10px;
    border-radius:10px;
    list-style:none;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.done{
    text-decoration:line-through;
    color:gray;
}

.footer{
    text-align:center;
    padding:20px;
    color:#666;
}
</style>

</head>

<body>

<div class="header">
    <h1>🤖 AI Todo Assistant</h1>
    <p>Ollama + Llama3.2 + Structured Output</p>
</div>

<div class="container">

<div class="card">
    <h2>📌 專案介紹</h2>

    <p>
        本專案利用 Ollama Llama3.2 分析自然語言，
        將提醒事項轉換成結構化 JSON 格式。
    </p>
</div>

<div class="card">
    <h2>⚙️ 執行方式</h2>

<pre>
python src/main.py
</pre>

</div>

<div class="card">
    <h2>💬 AI 解析範例</h2>

<pre>
輸入：
提醒我明天下午三點找老師討論論文

輸出：

{
  "title":"找老師討論論文",
  "time":"明天下午三點"
}
</pre>

</div>

<div class="card">
    <h2>✅ 互動式待辦清單</h2>

    <input id="taskInput"
           placeholder="輸入待辦事項">

    <button onclick="addTask()">
        新增
    </button>

    <ul id="taskList"></ul>

</div>

<div class="card">
    <h2>🚀 AI 使用說明</h2>

    <p>
        使用本地 Ollama Llama3.2 模型，
        將自然語言提醒事項轉換成 JSON 結構化資料，
        可應用於待辦事項管理系統。
    </p>

</div>

</div>

<div class="footer">
AI Todo Assistant | GitHub Pages Demo
</div>

<script>

function addTask(){

    const input =
        document.getElementById("taskInput");

    const text = input.value.trim();

    if(text==="") return;

    const li =
        document.createElement("li");

    li.innerHTML = `
        <span onclick="toggleTask(this)">
            ${text}
        </span>

        <button onclick="removeTask(this)">
            刪除
        </button>
    `;

    document
        .getElementById("taskList")
        .appendChild(li);

    input.value="";
}

function toggleTask(item){

    item.classList.toggle("done");
}

function removeTask(btn){

    btn.parentElement.remove();
}

</script>

</body>
</html>