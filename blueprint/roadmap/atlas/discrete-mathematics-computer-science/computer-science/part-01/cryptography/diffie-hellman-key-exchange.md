---
declaration: section
origin: cited
lean: Cslib.Crypto.PublicKey.gpow, Cslib.Crypto.PublicKey.dh_agree, Cslib.Crypto.PublicKey.dh_key_eq, Cslib.Crypto.PublicKey.gpowEquiv
statement: formalized
proof: formalized
---

# Diffie–Hellman key exchange

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/diffie-hellman-key-exchange/index.html).

## Group exponentiation with modular exponents

Let $G$ be a group, $q$ a natural number,
$g \in G$ and $a \in \mathbb{Z}/q\mathbb{Z}$. Then $g^a$ is defined as $g^n$, where $n$ is the
natural-number value of $a$: its representative in $\{0, \dots, q-1\}$ when $q > 0$, and $|a|$
when $q = 0$ (in which case $\mathbb{Z}/q\mathbb{Z} = \mathbb{Z}$).

Formalized by `Cslib.Crypto.PublicKey.gpow`, a definition declared in [CSLibExt/Crypto/PublicKey/DiffieHellman.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/PublicKey/DiffieHellman.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/diffie-hellman-key-exchange/index.html#gpow).

## Correctness of Diffie–Hellman key agreement

Let $G$ be a group, $q$ a natural number and
$g \in G$. For $x \in G$ and $c \in \mathbb{Z}/q\mathbb{Z}$ write $x^c$ for $x^n$, where $n$ is
the natural-number value of $c$: its representative in $\{0, \dots, q-1\}$ when $q > 0$, and
$|c|$ when $q = 0$ (in which case $\mathbb{Z}/q\mathbb{Z} = \mathbb{Z}$). Then
$(g^b)^a = (g^a)^b$ for all $a, b \in \mathbb{Z}/q\mathbb{Z}$.

Formalized by `Cslib.Crypto.PublicKey.dh_agree`, a theorem declared in [CSLibExt/Crypto/PublicKey/DiffieHellman.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/PublicKey/DiffieHellman.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/diffie-hellman-key-exchange/index.html#dh-agree).

## Value of the Diffie–Hellman shared key

Let $G$ be a group, $q$ a natural number and
$g \in G$ with $g^q = 1$. For $x \in G$ and $c \in \mathbb{Z}/q\mathbb{Z}$ write $x^c$ for $x^n$,
where $n$ is the natural-number value of $c$: its representative in $\{0, \dots, q-1\}$ when
$q > 0$, and $|c|$ when $q = 0$ (in which case $\mathbb{Z}/q\mathbb{Z} = \mathbb{Z}$). Then
$(g^b)^a = g^{ab}$ for all $a, b \in \mathbb{Z}/q\mathbb{Z}$, where $ab$ is the product in
$\mathbb{Z}/q\mathbb{Z}$.

Formalized by `Cslib.Crypto.PublicKey.dh_key_eq`, a theorem declared in [CSLibExt/Crypto/PublicKey/DiffieHellman.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/PublicKey/DiffieHellman.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/diffie-hellman-key-exchange/index.html#dh-key-eq).

## Exponentiation from a generator is a bijection

Let $G$ be a finite group of order $q$,
with $q \neq 0$, and let $g \in G$ generate $G$, that is, every element of $G$ is an integer
power of $g$. Then $a \mapsto g^a$ is a bijection from $\mathbb{Z}/q\mathbb{Z}$ to $G$, where
$g^a = g^n$ for the representative $n \in \{0, \dots, q-1\}$ of $a$. Its inverse is the
discrete logarithm to base $g$.

Formalized by `Cslib.Crypto.PublicKey.gpowEquiv`, a definition declared in [CSLibExt/Crypto/PublicKey/DiffieHellman.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/PublicKey/DiffieHellman.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/diffie-hellman-key-exchange/index.html#gpow-equiv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Diffie–Hellman key exchange](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/diffie-hellman-key-exchange/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/cryptography/diffie-hellman-key-exchange)
