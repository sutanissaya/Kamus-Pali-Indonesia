import streamlit as st
from streamlit.logger import get_logger
from streamlit.hello.utils import show_code
import altair as alt
import numpy as np
import pandas as pd

LOGGER = get_logger(__name__)

st.set_page_config(page_title="Dictionary Test", page_icon="🌴")
"""

setu: "m.  jembatan; jalan lintasan yang ditinggikan melewati rawa-rawa dsb; <b>~ghāta</b> a.  meruntuhkan jembatan (yang menghubungkan suatu tempat)."\n
sedeti: "(kaus. dari <b>sijjhati</b> )  membuat berpeluh, menghangatkan, menguapi."\n
senā: "f.  pasukan, (bala) tentara, laskar (yang terdiri dari <i>hatthī</i>, <i>assā</i>, <i>rathā</i>, <i>pattī</i>)."\n
senāsana: "nt. tempat berbaring dan duduk, tempat pernaungan di mana seseorang dapat duduk dan berbaring, tempat pembaringan, tempat tinggal, kediaman, peristirahatan; perlengkapan peristirahatan; <b>~cārika</b> a.  berkelana dari satu peristirahatan ke peristirahatan lainnya."\n
seyya: "a.  lebih baik, lebih bagus."\n
seyyathā: "adv. seperti, sebagaimana, bagaikan <b>~pi</b>  sama seperti, sebagaimana, bagaikan; <b>seyyathīdaṁ</b> sebagai berikut, yakni."\n
seyyā: "f.  tempat tidur, ranjang, katil, pembaringan, peraduan; dipan; kasur, tilam, bantal, karpet, seprei, tikar, pelapik lantai, penutup lantai, jangat hewan, kain duduk, lapik duduk, kain penutup; hal berbaring, tidur."\n
sela: "a.  berbatu-batu; m. batu, karang, kristal."\n
sevati: "melayani, bergaul dengan, mengambil jalan, berpaling kepada, mempraktikkan, memeluk, menggunakan."\n
sevanā: "f.  hal mengikuti, bergaul dengan, hidup bersama; hal meladeni."\n
sevāla: "m.  tanaman lumut <i>Blyxa actandra</i>; rumput air."\n
sesa(ka): "m.  sisa. [sisa ← Skt. ṡeṣa]"
soka: "m.  kesedihan, kepiluan."\n
sogata: "m.  pengikut Sang Sugata, pengikut Buddha, umat Buddha."\n
socati: "berdukacita atas, belasungkawa atas, berkabung atas, bersedih hati atas"
soceyya: "nt.  kemurnian."\n
soṇḍika: "m.  penyuling dan penjual minuman keras; pemabuk."\n
soṇḍikā: "f.  sulur tanaman menjalar; daging berlada; telaga."\n
sota: "1. nt. telinga, indra pendengaran; 2. m. nt.  arus, air bah, aliran air yang deras."\n
sotāpanna: "m.  orang yang telah masuk arus, orang yang telah mencapai tingkat kesucian pertama."\n
sotti: "f.  penggosok badan (perlengkapan mandi)."\n
sotthi: "f.  baik, aman, sejahtera, selamat (<i>Sotthi bhadante hotu rañño, sotthi janapadassāti</i>)."\n
sodheti: "(kaus. dari <b>sujjhati</b> )  membersihkan, memurnikan, memeriksa, mencari, memperbaiki, menyingkirkan, memutihkan (utang)."\n
sobbha: "m.  lubang, ceruk nan dalam."\n
sobhati: "bersinar, bercahaya, tampak elok, bagus, cemerlang; kaus. sobheti membuat gemerlapan, memperindah, menyemarakkan."\n
somanassa: "nt.  kegembiraan, kesukacitaan, kebahagiaan, kenyamanan batin."\n
sorivāra: "m.  Hari Sabtu."\n
svākkhāta: "a.  telah dibabarkan dengan baik; telah sempurna dipaparkan."\n
svāgata: "m.  sambutan, selamat datang."\n
svātana: "berkaitan dengan esok; <b>svātanāya</b> untuk hari berikutnya."\n
sve: "adv.  besok, keesokan harinya."\n
ha: "(kata penegas) hei, hallo, oh;  <i>iti ha</i> begitulah; <i>itihītihaṁ</i> begitu dan begitu; <i>heva  </i>yakni."\n
haṁsati: "meremang, merinding, menggidikkan bulu roma, tegak bulu badan, bulu romanya berdiri."\n
haṭṭha: "(pp dari <b>haṁsati</b> )  meremang, merinding, berdiri bulu romanya; gembira, bersuka cita, bahagia, girang."\n
hattha: "m.  tangan; lengan bawah; ukuran satu hasta (Menurut Bhikkhu Thanissaro, 1 hasta = 24 <b>aṅgula</b> ; 1 <b>sugatahattha</b>  = 50 cm); <b>~pāsa</b> m. seperentangan tangan, jangkauan tangan. [hasta ← Skt. hasta]"
hatthin: "m.  gajah."\n
hadaya: "m.  hati, batin; <b>~ṁgama</b> berkenan di hati; <b>~vatthu</b>  nt. landasan hati, landasan batin."\n
hanati: "menghantam, memukul, menggebuk, menghajar, mendera, menebah, mengirik; membunuh, menghancurkan, membinasakan, menyingkirkan; berak; pass. <b>haññati</b> ."\n
handa: "baiklah, sekarang, okei, marilah, aduh; sini; (<i>handāhaṁ</i>  baiklah, saya …)."\n
haraṇaka: "nt.  barang-barang yang bisa diangkut, barang-barang yang dapat dipindah-pindahkan, yang sedang dibawa, yang sedang dalam perjalanan."\n
harati: "membawa, membawa serta; mengambil, mengumpulkan, menawarkan, menyingkirkan, membawa pergi, merampas, mencuri, menghancurkan, membinasakan."\n
harāpeti: "menyebabkan dibawa, menawarkan."\n
harāyati: "merasa malu, merasa <i>tertekan</i> atau jengkel, dongkol, cemas."\n
harita: "a. hijau, hijau pucat, kekuning-kuningan; segar (<i>haritena gomayena paṭhaviṁ opuñjāpetvā</i>); nt. sayuran, hijauan, tanaman; <b>haritā</b>  f. emas."\n
halāhala: "m. 1. sejenis racun yang mematikan; 2. kegaduhan, kerusuhan, kekacauan."\n
hasati (hassati): "tertawa, bergembira; meringkik; kaus.  <b>hāseti</b>  membuat tertawa, menggembirakan, menyenangkan."\n
hasita: "(pp dari <b>hasati</b> ) tertawa; bergembira;  nt.  tawa, kegembiraan."\n
hāpeti: "1. mengabaikan, menanggalkan, menghilangkan; menunda; mengurangi; mengalahkan; hilang; 2. mempersembahkan, menyembah, memupuk, memelihara."\n
hāyati: "(pass. dari <b>jahati</b> ) ditinggalkan, berkurang, mengecil, lenyap, menghilang."\n
hāraka: "a.  membawa, mengambil, memperoleh, memindahkan; m. pembawa, pengambil."\n
hāriya: "a.  membawa."\n
hi: "sebab, karena, sungguh (<i>tañ hi tassa  </i>ia sungguh), tentu saja, memang; lah; <b>tena hi</b> baiklah kalau begitu, karena itu."\n
hita: "a.  bermanfaat; m. sahabat, penolong; nt. manfaat, kemaslahatan."\n
hitesin: "mengharapkan kesejahteraan pihak lain."\n
hiyyo: "adv.  kemarin."\n
hirañña: "nt.  emas, emas kepingan."\n
hiri (hirī): "f.  rasa malu, keseganan. (Vism 464 <i>kāyaduccaritādīhi hiriyatī ti hiri; lajjāyetaṁ adhivacanaṁ.</i>)"
hīna: "(pp dari <b>jahati</b> ) <i>rendah</i>, nista, hina-dina, terkutuk, inferior; kekurangan. [hina ← Skt. hīna]"
hīnāyāvatta: "m.  orang yang kembali ke kehidupan duniawi, orang yang kembali ke kehidupan rendah."\n
hīyo: "☞  <b>hiyyo</b>"
heṭṭhā: "di bawah."\n
heṭṭhimā: "a. terendah, lebih rendah; (tingkat) dasariah; <b>~tala</b>  lapisan terbawah."\n
hetu: "m.  “akar penyebab”, alasan, <i>sebab</i>, kondisi; demi."\n
heraññika: "m.  tukang emas, pakar emas, pandai emas, penukar mata uang; <b>~phalaka</b> m. nt. bilah/papan/meja sang penukar mata uang."\n
hemanta: "m.  musim dingin."\n
"""
