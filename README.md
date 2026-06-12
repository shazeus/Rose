# Aurelia - League of Legends için Zahmetsiz Skin Yönetimi

<div align="center">

  <img src="./assets/icon.png" alt="Aurelia Icon" width="128" height="128">

[![Installer](https://img.shields.io/badge/Installer-Windows-32A832)](https://github.com/aurelia/Aurelia/releases/latest) [![Fork](https://img.shields.io/badge/Fork-aurelia-32A832)](https://github.com/aurelia/Aurelia) [![Ko-Fi](https://img.shields.io/badge/KoFi-Donate-C03030?logo=ko-fi&logoColor=white)](https://ko-fi.com/aureliaapp) [![Discord](https://img.shields.io/discord/1490473857075642621?color=32A832&logo=discord&logoColor=white&label=Discord)](https://discord.com/invite/aureliaskins) [![Lisans](https://img.shields.io/badge/Lisans-MIT-C03030)](LICENSE) [![İndirmeler](https://img.shields.io/github/downloads/aurelia/Aurelia/total?color=32A832&label=Fork%20Indirmeleri)](https://github.com/aurelia/Aurelia/releases/latest)

</div>

---

## Genel Bakış

Bu depo, **aurelia/Aurelia** forkudur. Forkun amacı Aurelia'un mevcut çalışma akışını korurken paketleme, görünen proje linkleri, League Client içi panel metinleri, fork notları ve güncelleme kaynağı gibi fork sahibine ait kısımları temiz hale getirmektir.

Aurelia, League of Legends için açık kaynaklı bir skin yönetim aracıdır. Uygulama sistem tepsisinde çalışır, şampiyon seçimi sırasında seçilen skinleri takip eder ve oyun yüklenirken yerel görüntü varlıklarını uygular.

Aurelia, [Pengu Loader](https://github.com/Tariolle/AURELIA-Pengu) altyapısını kullanarak League Client içine JavaScript eklentileri entegre eder. Proje yerel model/doku görünüm değişkenleriyle çalışır; ağ verisini, bellek durumunu veya oynanış mekaniklerini manipüle etmeyi hedeflemez ve rekabet avantajı sunmaz.

## Bu Forkta Yapılan Geliştirmeler

- README, fork kullanıcıları için Türkçe ve daha açık hale getirildi.
- README, installer metadata, plugin metadata, sistem tepsisi başlıkları ve League Client içindeki SettingsPanel GitHub linkleri `aurelia/Aurelia` forkuna yönlendirildi.
- [FORK_NOTES.md](FORK_NOTES.md) eklendi; forkta hangi alanların özelleştirildiği ve runtime akışa dokunulmadığı ayrıca belgelendi.
- Launcher updater artık varsayılan olarak `aurelia/Aurelia` release'lerini kontrol eder.
- Özel build ve test senaryoları için updater release kaynağı `AURELIA_RELEASE_REPO` veya `AURELIA_RELEASE_API` ortam değişkenleriyle değiştirilebilir.
- Updater release kaynağı için küçük regresyon testleri eklendi.
- League Client içindeki SettingsPanel'e `Aurelia` kimlik kartı, canlı ayar özeti ve daha düzenli aksiyon butonları eklendi.
- ChromaWheel ve FormsWheel panellerine seçenek sayacı, kısa kullanım metni, Aurelia başlığı ve klavye ile seçilebilir buton etiketleri eklendi.
- Party Mode panel başlığı ve açıklaması fork kimliğiyle daha anlaşılır hale getirildi.

## Mimari

Aurelia üç ana parçadan oluşur:

### Python Backend

- **LCU API Entegrasyonu**: League Client Update (LCU) API ile iletişim kurar.
- **Skin Uygulama Akışı**: Riot Vanguard ile uyumlu olacak şekilde skin uygulama sürecini yönetir.
- **WebSocket Köprüsü**: Frontend eklentileriyle anlık iletişim kurmak için WebSocket sunucusu çalıştırır.
- **Skin Yönetimi**: Skin dosyalarını [LeagueSkins deposundan](https://github.com/Alban1911/LeagueSkins) indirir ve düzenler.
- **Party Mode**: Aynı lobideki arkadaşlar arasında skin seçimlerini Cloudflare WebSocket relay üzerinden paylaşır.
- **Oyun İzleme**: Oyun durumunu, şampiyon seçimi fazlarını ve loadout geri sayımını takip eder.
- **Otomatik Güncelleyici**: GitHub release'lerini kontrol eder ve uygun güncellemeyi kullanıcıya sunar.
- **Analitik**: Yapılandırılabilir arka plan pingleriyle benzersiz kullanıcı sayımını takip eder.

### Cloudflare Workers

- **aurelia-party-relay**: Party odalarını yöneten Durable Object tabanlı WebSocket relay servisidir. Oda başına en fazla 10 üyeyi destekler.

### Pengu Loader Eklentileri

- **AURELIA-UI**: Şampiyon seçimindeki kilitli skin önizlemelerini açarak hover etkileşimlerini etkinleştirir.
- **AURELIA-SkinMonitor**: Seçili skin adını takip eder ve Python backend'e WebSocket ile iletir.
- **AURELIA-CustomWheel**: Hover edilen skinler için mod metadata bilgisini gösterir ve mods klasörüne hızlı erişim sağlar.
- **AURELIA-ChromaWheel**: Her chroma varyantını seçmek için gelişmiş chroma arayüzü sunar.
- **AURELIA-FormsWheel**: Birden fazla forma sahip skinler için özel form seçim arayüzü sağlar.
- **AURELIA-SettingsPanel**: League Client içinden erişilebilen Aurelia ayar panelidir.
- **AURELIA-RandomSkin**: Rastgele skin seçimi özelliğini sağlar.
- **AURELIA-HistoricMode**: Her şampiyon için son kullanılan skine hızlı erişim verir.
- **AURELIA-PartyMode**: Lobi ve şampiyon seçiminde skin paylaşımı, bağlı kişiler ve arkadaş seçimlerini gösteren paneli sağlar.
- **AURELIA-Jade**: Client için border, arka plan, banner, ikon, unvan ve win/loss görünüm özelleştirmeleri sunar.

## Nasıl Çalışır?

1. Aurelia açılış sırasında **[Pengu Loader](https://github.com/Tariolle/AURELIA-Pengu)** entegrasyonunu başlatır.
2. `AURELIA-SkinMonitor`, şampiyon seçiminde hover edilen skin bilgisini algılar.
3. Python backend, gelen seçimi ve oyun fazını takip eder.
4. Oyun yüklenirken seçilen skinin yerel varlıkları uygulanır.
5. Skin yalnızca yerel görünüm olarak yüklenir; oynanış etkilenmez.

## Özellikler

- **Akıllı Uygulama**: Zaten sahip olunan skinleri gereksiz yere uygulamamaya çalışır.
- **Çoklu Dil Desteği**: Farklı League Client dilleriyle çalışacak şekilde tasarlanmıştır.
- **Modüler Plugin Yapısı**: UI ve istemci davranışları Pengu Loader eklentileriyle ayrılmıştır.
- **Fork Dostu Güncelleme**: Bu fork, güncellemeleri `aurelia/Aurelia` release'lerinden kontrol eder.
- **Test Edilebilir Release Kaynağı**: `AURELIA_RELEASE_REPO=owner/repo` veya `AURELIA_RELEASE_API=https://...` ile updater hedefi değiştirilebilir.
- **Açık Kaynak**: Kod okunabilir, incelenebilir ve fork üzerinden geliştirilebilir.

## Gereksinimler

- **Windows 10/11**
- **League of Legends** kurulu olmalıdır.
- **Injection DLL**: Kullanıcının kendi imzalı DLL dosyasını sağlaması gerekir.

### DLL Gereksinimi

DMCA kısıtlamaları nedeniyle Aurelia injection DLL dosyasını dağıtmaz. Kullanıcı bu dosyayı yetkili bir kaynaktan edinmeli ve kendi kod imzalama sertifikası ile imzalamalıdır.

İlk açılışta Aurelia gerekli klasörü açar ve kullanıcıdan ilgili dosyayı yerleştirmesini ister.

## Kurulum

1. En güncel fork installer dosyasını [Releases](https://github.com/aurelia/Aurelia/releases/latest) sayfasından indirin.
2. Installer'ı Yönetici olarak çalıştırın.
3. Aurelia'u Başlat Menüsü veya masaüstü kısayolundan açın.

## Fork Ayarları

Updater varsayılan olarak bu fork release'lerini kullanır:

```powershell
https://github.com/aurelia/Aurelia/releases/latest
```

Test veya özel build için kaynak değiştirme:

```powershell
$env:AURELIA_RELEASE_REPO = "kullanici/Aurelia"
```

Tam API URL'i vermek için:

```powershell
$env:AURELIA_RELEASE_API = "https://api.github.com/repos/kullanici/Aurelia/releases/latest"
```

## Katkı

Geliştirme kurulumu ve proje yapısı için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakın.

Fork üzerinde çalışırken:

- Runtime injection akışını değiştiren commitleri ayrı tutun.
- Upstream ile karşılaştırması kolay, küçük ve net commitler tercih edin.
- League Client entegrasyonuna dokunmadan önce upstream değişikliklerini kontrol edin.

## Yasal Uyarı

Bu proje Riot Games tarafından desteklenmez ve Riot Games ile resmi bir bağlantısı yoktur. Riot Games ve ilgili tüm markalar Riot Games, Inc. şirketinin ticari markaları veya tescilli markalarıdır.

Custom skin kullanımında sorumluluk kullanıcıya aittir. Oyun içinde skin araçlarını tartışmayın veya reklamını yapmayın.

## Destek

Upstream Aurelia topluluğunu desteklemek isterseniz:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/aureliaapp)

---

**Aurelia** - _League, unlocked._
