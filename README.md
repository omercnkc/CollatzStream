# 🚀 CollatzStream

**A secure, rolling stream cipher based on the chaotic nature of the Collatz Conjecture, featuring 128-bit block encryption, dynamic state repair, and 32-bit IV randomization.** :contentReference[oaicite:0]{index=0}

---

## 📌 Overview

**CollatzStream** Python ile geliştirilmiş, Collatz varsayımından türetilmiş bir **kayan anahtar (stream) şifreleme algoritmasıdır**.  
Bu proje, deterministik Collatz dizilerinden 128-bitlik anahtar akışı üreterek veri şifreleme ve çözme sağlar. :contentReference[oaicite:1]{index=1}

> ⚠️ _Bu uygulama eğitim/deney amaçlıdır. Modern ve incelenmiş kriptografik primitiflerin yerine kullanılmamalıdır._ :contentReference[oaicite:2]{index=2}

---

## 🔐 Features

- 📦 **128-bit blok** tabanlı şifreleme  
- 🎯 **Kayan anahtar stream cipher** uygulaması  
- 🔄 **Dinamik durum onarımı**  
- 🔑 **32-bit IV (Initialization Vector) randomizasyonu  
- 🐍 Saf Python ile yazılmış (Python 3.10+ gerektirir) :contentReference[oaicite:3]{index=3}

---

## 🧠 How It Works

CollatzStream algoritması Collatz dizilerini matematiksel olarak işler ve bunları şifreleme anahtarı olarak kullanır. Başlangıç durumundan sonra iki farklı Collatz dizisi elde edilir ve bu diziler birlikte **fermuar (zipper) yöntemi** ile 128-bitlik anahtar bloğu üretir. :contentReference[oaicite:4]{index=4}

---

## 🚀 Quick Start

### 🛠 Requirements

- Python 3.10 veya üstü

---

### 📁 Clone the repository

```bash
git clone https://github.com/omercnkc/CollatzStream.git
cd CollatzStream

