---
declaration: section
origin: cited
lean: Cslib.Crypto.PublicKey.RSA.pow_eq_self_of_modEq, Cslib.Crypto.PublicKey.RSA.pow_eq_pow_of_modEq, Cslib.Crypto.PublicKey.RSA.one_le_mod, Cslib.Crypto.PublicKey.RSA.Key, Cslib.Crypto.PublicKey.RSA.Key.n, Cslib.Crypto.PublicKey.RSA.Key.encrypt, Cslib.Crypto.PublicKey.RSA.Key.decrypt, Cslib.Crypto.PublicKey.RSA.Key.crt
statement: formalized
proof: formalized
---

# RSA cryptosystem

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html).

## RSA

## Fermat's little theorem with exponents congruent to one

Let $p$ be a prime and let
$k \ge 1$ be a natural number with $k \equiv 1 \pmod{p - 1}$. Then $x^k = x$ for every
$x \in \mathbb{Z}/p\mathbb{Z}$.

Formalized by `Cslib.Crypto.PublicKey.RSA.pow_eq_self_of_modEq`, a theorem declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#pow-eq-self-of-mod-eq).

## Fermat's little theorem for congruent exponents

Let $p$ be a prime and let $a$ and $b$
be natural numbers with $a, b \ge 1$ and $a \equiv b \pmod{p - 1}$. Then $x^a = x^b$ for every
$x \in \mathbb{Z}/p\mathbb{Z}$.

Formalized by `Cslib.Crypto.PublicKey.RSA.pow_eq_pow_of_modEq`, a theorem declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#pow-eq-pow-of-mod-eq).

## Positivity of the reduced RSA exponent

Let $p$, $e$ and $d$ be natural numbers with
$p > 2$ and $ed \equiv 1 \pmod{p - 1}$. Then $d \bmod (p - 1) \ge 1$.

Otherwise $p - 1$ divides $ed$, contradicting $ed \equiv 1 \pmod{p - 1}$.

Formalized by `Cslib.Crypto.PublicKey.RSA.one_le_mod`, a theorem declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#one-le-mod).

## RSA key

A textbook RSA key consists of distinct primes $p$ and $q$ and natural numbers $e$
(the public exponent) and $d$ (the private exponent) such that $ed \equiv 1 \pmod{p - 1}$ and
$ed \equiv 1 \pmod{q - 1}$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key`, a structure declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#key).

## RSA modulus

The modulus of an RSA key with primes $p$ and $q$ is $n = pq$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.n`, a definition declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#n).

## RSA encryption

For an RSA key with modulus $n = pq$ and public exponent $e$, encryption is
the map $\mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ given by $m \mapsto m^e$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.encrypt`, a definition declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#encrypt).

## RSA decryption

For an RSA key with modulus $n = pq$ and private exponent $d$, decryption is
the map $\mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ given by $c \mapsto c^d$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.decrypt`, a definition declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#decrypt).

## Chinese remainder isomorphism for an RSA modulus

For an RSA key with distinct primes $p$,
$q$ and modulus $n = pq$, this is the ring isomorphism
$\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z}$ of the Chinese
remainder theorem, sending $x$ to $(x \bmod p, x \bmod q)$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.crt`, a definition declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#crt).

## Checking a power identity through the Chinese remainder theorem

Let an RSA key have
primes $p$ and $q$ and modulus $n$, let $k$ be a natural number and $x \in \mathbb{Z}/n\mathbb{Z}$,
and let $(x_p, x_q) \in \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z}$ be the image of $x$
under the Chinese remainder isomorphism. If $x_p^k = x_p$ and $x_q^k = x_q$, then $x^k = x$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.pow_eq_self_of_crt`, a theorem declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#pow-eq-self-of-crt).

## RSA exponent identity

For an RSA key with modulus $n$ and exponents $e$ and $d$, every
$x \in \mathbb{Z}/n\mathbb{Z}$ satisfies $x^{ed} = x$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.pow_ed`, a theorem declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#pow-ed).

## Correctness of textbook RSA

Decryption inverts encryption on every message, including
messages that are not coprime to `n`.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.decrypt_encrypt`, a theorem declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#decrypt-encrypt).

## RSA encryption is a bijection

For an RSA key with modulus $n = pq$ and public exponent
$e$, the encryption map $m \mapsto m^e$ is a bijection from $\mathbb{Z}/n\mathbb{Z}$ to itself.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.encrypt_bijective`, a theorem declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#encrypt-bijective).

## Correctness of textbook RSA on natural numbers

For an RSA key with modulus $n = pq$ and
exponents $e$, $d$, every natural number $m < n$ satisfies $(m^e \bmod n)^d \bmod n = m$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.decrypt_encrypt_nat`, a theorem declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#decrypt-encrypt-nat).

## RSA-CRT decryption

Let $(p, q, e, d)$ be an RSA key with modulus $n = pq$. For natural
numbers $d_p$, $d_q$ and $c \in \mathbb{Z}/n\mathbb{Z}$, let $c_p$ and $c_q$ be the images of $c$ in
$\mathbb{Z}/p\mathbb{Z}$ and $\mathbb{Z}/q\mathbb{Z}$. RSA-CRT decryption of $c$ with the exponents
$d_p$ and $d_q$ is the element of $\mathbb{Z}/n\mathbb{Z}$ that corresponds to the pair
$(c_p^{d_p}, c_q^{d_q})$ under the Chinese remainder isomorphism
$\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z}$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.crtDecrypt`, a definition declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#crt-decrypt).

## RSA-CRT decryption is correct

Let $(p, q, e, d)$ be an RSA key with modulus $n = pq$, and
let $d_p, d_q \ge 1$ be natural numbers with $d_p \equiv d \pmod{p - 1}$ and
$d_q \equiv d \pmod{q - 1}$. Then for every $c \in \mathbb{Z}/n\mathbb{Z}$, RSA-CRT decryption of
$c$ with the exponents $d_p$ and $d_q$ equals the RSA decryption $c^d$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.crtDecrypt_eq`, a theorem declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#crt-decrypt-eq).

## RSA-CRT decryption with the standard exponents

Let $(p, q, e, d)$ be an RSA key with
modulus $n = pq$ in which both primes are odd, that is $p > 2$ and $q > 2$. Then for every
$c \in \mathbb{Z}/n\mathbb{Z}$, RSA-CRT decryption of $c$ with the exponents
$d_p = d \bmod (p - 1)$ and $d_q = d \bmod (q - 1)$ equals the RSA decryption $c^d$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.crtDecrypt_mod_eq`, a theorem declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#crt-decrypt-mod-eq).

## RSA key from the totient condition

Given distinct primes $p$ and $q$ and natural
numbers $e$ and $d$ with $ed \equiv 1 \pmod{\varphi(pq)}$, where $\varphi$ is Euler's totient
function, this is the RSA key with primes $p$ and $q$, public exponent $e$ and private exponent
$d$. Its conditions $ed \equiv 1 \pmod{p - 1}$ and $ed \equiv 1 \pmod{q - 1}$ hold because
$\varphi(pq) = (p - 1)(q - 1)$.

Formalized by `Cslib.Crypto.PublicKey.RSA.Key.ofTotient`, a definition declared in [CSLibExt/Crypto/PublicKey/RSA.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/RSA.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html#of-totient).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: RSA cryptosystem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/cryptography/public-key/rsa-cryptosystem)
