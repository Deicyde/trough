---
declaration: section
origin: cited
lean: Cslib.Crypto.Signatures.Lamport.publicKey, Cslib.Crypto.Signatures.Lamport.sign, Cslib.Crypto.Signatures.Lamport.Verify, Cslib.Crypto.Signatures.Lamport.verify_sign, Cslib.Crypto.Signatures.Lamport.Forger, Cslib.Crypto.Signatures.Lamport.Forger.Wins, Cslib.Crypto.Signatures.Lamport.forgeGame, Cslib.Crypto.Signatures.Lamport.invertGame
statement: formalized
proof: formalized
---

# Lamport signature

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html).

## Lamport public key

For a function $f : X \to Y$ and a secret key
$sk : \{0, \dots, \ell - 1\} \times \{0, 1\} \to X$, the public key is the map
$pk : \{0, \dots, \ell - 1\} \times \{0, 1\} \to Y$ with $pk(i, b) = f(sk(i, b))$.

Formalized by `Cslib.Crypto.Signatures.Lamport.publicKey`, a definition declared in [CSLibExt/Crypto/Signatures/Lamport.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Signatures/Lamport.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html#public-key).

## Lamport signing

The signature of a message $m \in \{0, 1\}^\ell$ under a secret key
$sk : \{0, \dots, \ell - 1\} \times \{0, 1\} \to X$ is $\sigma \in X^\ell$ with
$\sigma_i = sk(i, m_i)$ for every position $i < \ell$.

Formalized by `Cslib.Crypto.Signatures.Lamport.sign`, a definition declared in [CSLibExt/Crypto/Signatures/Lamport.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Signatures/Lamport.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html#sign).

## Lamport verification

Let $f : X \to Y$. A signature $\sigma \in X^\ell$ on a message
$m \in \{0, 1\}^\ell$ is valid for a public key $pk : \{0, \dots, \ell - 1\} \times \{0, 1\} \to Y$
when $f(\sigma_i) = pk(i, m_i)$ for every position $i < \ell$.

Formalized by `Cslib.Crypto.Signatures.Lamport.Verify`, a definition declared in [CSLibExt/Crypto/Signatures/Lamport.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Signatures/Lamport.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html#verify).

## Correctness of Lamport signatures

Let $f : X \to Y$. For every secret key
$sk : \{0, \dots, \ell - 1\} \times \{0, 1\} \to X$ and every message $m \in \{0, 1\}^\ell$, the
Lamport signature of $m$ under $sk$ is valid for $m$ under the public key of $sk$.

Formalized by `Cslib.Crypto.Signatures.Lamport.verify_sign`, a theorem declared in [CSLibExt/Crypto/Signatures/Lamport.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Signatures/Lamport.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html#verify-sign).

## One-time forger

A one-time forger for messages of length $\ell$, with random coins in a
set $R$, consists of two maps. The first takes a public key
$pk : \{0, \dots, \ell - 1\} \times \{0, 1\} \to Y$ and coins $r \in R$ and returns the message
$m \in \{0, 1\}^\ell$ whose signature the forger requests. The second takes a public key, a
signature $\sigma \in X^\ell$ and coins $r$ and returns a message $m' \in \{0, 1\}^\ell$ together
with a signature $\sigma' \in X^\ell$.

Formalized by `Cslib.Crypto.Signatures.Lamport.Forger`, a structure declared in [CSLibExt/Crypto/Signatures/Lamport.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Signatures/Lamport.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html#forger).

## Winning the Lamport one-time forgery game

Let $X$ be a nonempty finite set, $Y$ a set
with decidable equality, $f : X \to Y$ a function, and $\ell$ a message length; messages are bit
strings $m = (m_0, \dots, m_{\ell-1})$. A one-time forger $A$ with random coins from a nonempty
finite set $R$ wins against a secret key $sk$, which assigns $sk(i, b) \in X$ to each position
$i < \ell$ and bit $b$, with coins $r \in R$ when the following holds. Let $pk$ be the public key
of $sk$, given by $pk(i, b) = f(sk(i, b))$; let $m$ be the message that $A$ chooses from $pk$ and
$r$; and let $(m', \sigma')$ be the message and signature that $A$ outputs from $pk$, the
signature $i \mapsto sk(i, m_i)$ of $m$ under $sk$, and $r$. Then $m' \ne m$, and $\sigma'$ is a
valid signature on $m'$ for $pk$: $f(\sigma'_i) = pk(i, m'_i)$ for every $i < \ell$.

Formalized by `Cslib.Crypto.Signatures.Lamport.Forger.Wins`, a definition declared in [CSLibExt/Crypto/Signatures/Lamport.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Signatures/Lamport.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html#wins).

## One-time forgery game

Let $f : X \to Y$ with $X$ finite and nonempty, and let $A$ be a
one-time forger for messages of length $\ell$ with random coins in a finite nonempty set $R$. The
one-time forgery game is the distribution on $\{\mathrm{true}, \mathrm{false}\}$ obtained by drawing
a secret key $sk : \{0, \dots, \ell - 1\} \times \{0, 1\} \to X$ and coins $r \in R$ uniformly and
independently, and returning whether $A$ wins against $sk$ with coins $r$.

Formalized by `Cslib.Crypto.Signatures.Lamport.forgeGame`, a definition declared in [CSLibExt/Crypto/Signatures/Lamport.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Signatures/Lamport.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html#forge-game).

## One-wayness game

Let $f : X \to Y$ with $X$ finite and nonempty, and let $I$ be an
inverter with random coins in a finite nonempty set $\Omega$: given $y \in Y$ and coins
$\omega \in \Omega$ it either outputs some $x' \in X$ or fails. The one-wayness game for $f$ is the
distribution on $\{\mathrm{true}, \mathrm{false}\}$ obtained by drawing $x \in X$ and
$\omega \in \Omega$ uniformly and independently and returning true exactly when $I$, run on $f(x)$
with coins $\omega$, outputs some $x'$ with $f(x') = f(x)$.

Formalized by `Cslib.Crypto.Signatures.Lamport.invertGame`, a definition declared in [CSLibExt/Crypto/Signatures/Lamport.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Signatures/Lamport.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html#invert-game).

## Planted public key

Let $f : X \to Y$. Given a secret key
$sk : \{0, \dots, \ell - 1\} \times \{0, 1\} \to X$, a position $(i, b)$ and a value $y \in Y$, the
planted public key takes the value $y$ at $(i, b)$ and the value $f(sk(j, c))$ at every other
position $(j, c)$.

Formalized by `Cslib.Crypto.Signatures.Lamport.plant`, a definition declared in [CSLibExt/Crypto/Signatures/Lamport.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Signatures/Lamport.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html#plant).

## Inverter built from a forger

Let $f : X \to Y$, let $A$ be a one-time forger for messages
of length $\ell$ with coins in $R$, and let $y \in Y$. The inverter's coins are a position $(i, b)$
with $i < \ell$ and $b \in \{0, 1\}$, a secret key
$sk : \{0, \dots, \ell - 1\} \times \{0, 1\} \to X$ and forger coins $r \in R$. It forms the
public key $pk$ with $pk(i, b) = y$ and $pk(j, c) = f(sk(j, c))$ for every other $(j, c)$, and
runs $A$ on $pk$ with coins $r$ to obtain the message $m$ whose signature $A$ requests. If
$m_i = b$ it fails. Otherwise it hands $A$ the signature $(sk(j, m_j))_{j < \ell}$ of $m$ under
$sk$ and obtains a forgery $(m', \sigma')$; it outputs $\sigma'_i$ if $m'_i = b$ and fails
otherwise.

Formalized by `Cslib.Crypto.Signatures.Lamport.invert`, a definition declared in [CSLibExt/Crypto/Signatures/Lamport.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Signatures/Lamport.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html#invert).

## Security reduction for Lamport one-time signatures

Let $f : X \to Y$ be a function on a
finite nonempty set $X$, let $\ell \ge 1$ be the message length, and let $A$ be a one-time forger
whose random coins range over a finite nonempty set $R$. Then the probability that $A$ wins the
one-time forgery game against the Lamport scheme built from $f$ is at most $2\ell$ times the
probability that the inverter built from $A$ wins the one-wayness game for $f$.

This is the reduction behind Katz and Lindell, Theorem 12.16: if $f$ is one-way, then Lamport's
scheme is one-time secure.

Formalized by `Cslib.Crypto.Signatures.Lamport.forgeGame_le`, a theorem declared in [CSLibExt/Crypto/Signatures/Lamport.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Signatures/Lamport.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html#forge-game-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lamport signature](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/lamport-signature/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/cryptography/lamport-signature)
