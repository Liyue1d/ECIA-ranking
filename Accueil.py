import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = Image.open('talan.png')

# st.image(image, width=20)


st.markdown("<h1 style='text-align: center'>ECIA</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Comparison of speed and energy consumption of AI languages</h4>",
            unsafe_allow_html=True)

option = st.selectbox('Energy or runtime?', ('Energy', 'Runtime'))
st.write('You selected:', option)

if option == 'Energy':
    x = st.slider('Estimated consumed energy using C language in mWh', min_value=1, max_value=100)
else:
    x = st.slider('Estimated program runtime using C language in minutes', min_value=1, max_value=100)

st.caption(
    "\* Estimated on a Linux Ubuntu Server 16.10 operating system,"
    " kernel version 4.8.0-22-generic, with 16GB of RAM, a Haswell "
    "Intel(R) Core(TM) i5-4460 CPU @ 3.20GHz",
    unsafe_allow_html=False)

if option == 'Energy':
    C = 1.00 * x
    Rust = 1.03 * x
    Cpp = 1.34 * x
    Ada = 1.70 * x
    Java = 1.98 * x
    Pascal = 2.14 * x
    Chapel = 2.18 * x
    Lisp = 2.27 * x
    Ocaml = 2.4 * x
    Fortran = 2.52 * x
    Swift = 2.79 * x
    Haskell = 3.10 * x
    Csharp = 3.14 * x
    Go = 3.23 * x
    Dart = 3.83 * x
    Fsharp = 4.13 * x
    JavaScript = 4.45 * x
    Racket = 7.91 * x
    TypeScript = 21.5 * x
    Hack = 24.02 * x
    PHP = 29.3 * x
    Erlang = 42.23 * x
    Lua = 45.98 * x
    Jruby = 46.54 * x
    Ruby = 69.91 * x
    Python = 75.88 * x
    Perl = 79.58 * x
    SWIProlog = 124.19 * x
    SICStusProlog = 130.04 * x

else:
    C = 1.00 * x
    Rust = 1.04 * x
    Cpp = 1.56 * x
    Ada = 1.85 * x
    Java = 1.89 * x
    Chapel = 2.14 * x
    Go = 2.83 * x
    Pascal = 3.02 * x
    Ocaml = 3.09 * x
    Csharp = 3.14 * x
    Lisp = 3.40 * x
    Haskell = 3.55 * x
    Swift = 4.20 * x
    Fortran = 4.20 * x
    Fsharp = 6.30 * x
    JavaScript = 6.52 * x
    Dart = 6.67 * x
    Racket = 11.27 * x
    Hack = 26.99 * x
    PHP = 27.64 * x
    Erlang = 36.71 * x
    Jruby = 43.44 * x
    TypeScript = 46.20 * x
    Ruby = 59.34 * x
    Perl = 65.79 * x
    Python = 71.90 * x
    Lua = 82.91 * x
    SWIProlog = 131.85 * x
    SICStusProlog = 415.85 * x

hist_data = np.array([C, Rust, Cpp, Ada, Java, Chapel, Go, Pascal, Ocaml, Csharp, Lisp,
                      Haskell, Swift, Fortran, Fsharp, JavaScript, Dart, Racket, Hack, PHP, Erlang,
                      Jruby, TypeScript, Ruby, Perl, Python, Lua, SWIProlog, SICStusProlog])
group_labels = np.array(['C', 'Rst', 'C++', 'Ada', 'Jav', 'Chp', 'Go', 'Psc', 'Ocl',
                         'C#', 'Lsp', 'Hsk', 'Swif', 'For', 'F#', 'JS',
                         'Drt', 'Rck', 'Hck', 'PHP', 'Erl', 'Jrb', 'TS', 'Rub',
                         'Prl', 'Pyt', 'Lua', 'SWI', 'SIC'])

idx = np.argsort(hist_data)
sorted_hist_data = sorted(hist_data)
sorted_group_labels = group_labels[idx]

fig, ax = plt.subplots()
if option == 'Energy':
    plt.ylabel('Consumed energy (mWh)', size=10)
else:
    plt.ylabel('Runtime (min)')
plt.xlabel('Language', size=6)
plt.rcParams["font.size"] = 5.5
ax.vlines(sorted_group_labels, 0, sorted_hist_data, label=['test', 'test23'], color=['C0',
                                                                                     'C1', 'C2', 'C3', 'C4', 'C5', 'C6',
                                                                                     'C7', 'C8', 'C9'])
st.pyplot(fig)

"LEGEND"

leg = "Rst: Rust | Jav: Java | Chp: Chapel | Psc: Pascal | Ocl: Ocaml | Lsp: Lisp |Hsk: Hask |" \
      " Swif: Swift |For: Fortran | JS: JavaScript | Drt: Dart | Rck: Rack | Hck: Hack |" \
      " Erl: Erlang | Jrb: Jruby | TS: TypeScript | Rub: Ruby | Prl: Perl | Pyt: Python" \
      " | SWI: SWI-Prolog | SIC: SICStus Prolog"


leg