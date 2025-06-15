#!/bin/bash

# Git deposunu başlat
git init

# Kullanıcıdan eklenecek dosyanın adını al
echo "Dosya adını giriniz (formatıyla birlikte örn: dosya.txt):"
read dad

# Dosyayı ekle
git add "$dad"

# Commit işlemi
git commit -m "first commit"

# Kullanıcıdan branch adı al (main mi master mı?)
echo "Ana branch adı nedir? (main / master):"
read mm
git branch -M "$mm"

# Uzak repo adresini al
echo "Git uzaktaki adresi giriniz (örnek: https://github.com/kullanici/repo.git):"
read dadr
git remote add origin "$dadr"

# Uzak repo'ya push et
git push -u origin "$mm"
