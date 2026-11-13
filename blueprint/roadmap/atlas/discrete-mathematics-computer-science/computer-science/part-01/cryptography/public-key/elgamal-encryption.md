---
declaration: section
origin: cited
lean: Cslib.Crypto.PublicKey.ElGamal.publicKey, Cslib.Crypto.PublicKey.ElGamal.encrypt, Cslib.Crypto.PublicKey.ElGamal.decrypt, Cslib.Crypto.PublicKey.ElGamal.decrypt_encrypt, Cslib.Crypto.PublicKey.ElGamal.pick, Cslib.Crypto.PublicKey.ElGamal.Adversary, Cslib.Crypto.PublicKey.ElGamal.eavGame, Cslib.Crypto.PublicKey.ElGamal.eavAdvantage
statement: formalized
proof: formalized
---

# ElGamal encryption

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html).

## ElGamal

## ElGamal public key

Let $G$ be a commutative group with a fixed element $g$ and let $q$ be
a natural number. The public key of a secret key $x \in \mathbb{Z}/q$ is $h = g^{v(x)} \in G$,
where $v(x) \in \{0, \dots, q - 1\}$ is the least nonnegative representative of $x$ if $q \ge 1$,
and $v(x) = |x|$ if $q = 0$ (when $\mathbb{Z}/0 = \mathbb{Z}$).

Formalized by `Cslib.Crypto.PublicKey.ElGamal.publicKey`, a definition declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#public-key).

## ElGamal encryption

Let $G$ be a commutative group with a fixed element $g$ and let $q$ be
a natural number. The ElGamal encryption of a message $m \in G$ under the public key $h \in G$
with randomness $y \in \mathbb{Z}/q$ is the pair $(g^y, h^y m) \in G \times G$. Here a power
$k^a$ with $k \in G$ and $a \in \mathbb{Z}/q$ means $k^{v(a)}$, where $v(a) \in \{0, \dots, q - 1\}$
is the least nonnegative representative of $a$ if $q \ge 1$, and $v(a) = |a|$ if $q = 0$ (when
$\mathbb{Z}/0 = \mathbb{Z}$).

Formalized by `Cslib.Crypto.PublicKey.ElGamal.encrypt`, a definition declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#encrypt).

## ElGamal decryption

Let $G$ be a commutative group and $q$ a natural number. For
$a \in \mathbb{Z}/q\mathbb{Z}$ and $c \in G$ write $c^a$ for $c^{\operatorname{val}(a)}$, where
$\operatorname{val}(a) \in \mathbb{N}$ is the representative of $a$ in $\{0, \dots, q-1\}$ if
$q \ge 1$ and $|a|$ if $q = 0$. Decrypting a ciphertext $(c_1, c_2) \in G \times G$ with the
secret key $x \in \mathbb{Z}/q\mathbb{Z}$ gives $c_2 \cdot (c_1^x)^{-1}$.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.decrypt`, a definition declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#decrypt).

## Correctness of ElGamal

Let $G$ be a commutative group, $g \in G$ and $q$ a natural
number. For $a \in \mathbb{Z}/q\mathbb{Z}$ and $c \in G$ write $c^a$ for
$c^{\operatorname{val}(a)}$, where $\operatorname{val}(a) \in \mathbb{N}$ is the representative
of $a$ in $\{0, \dots, q-1\}$ if $q \ge 1$ and $|a|$ if $q = 0$. For every secret key
$x \in \mathbb{Z}/q\mathbb{Z}$, every message $m \in G$ and every encryption randomness
$y \in \mathbb{Z}/q\mathbb{Z}$, decrypting with $x$ the ElGamal encryption of $m$ under the
public key $g^x$ with randomness $y$ returns $m$.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.decrypt_encrypt`, a theorem declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#decrypt-encrypt).

## Message selected by the challenge bit

Let $G$ be a finite commutative group. For a pair
of messages $(m_0, m_1) \in G \times G$ and a bit $b$, the selected message is $m_1$ if $b$ is
true and $m_0$ if $b$ is false.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.pick`, a definition declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#pick).

## ElGamal eavesdropping adversary

Given a type $G$ of public keys and messages and a type
$R$ of random coins, an eavesdropping adversary consists of a choice function, which maps a public
key $h \in G$ and coins $r \in R$ to a pair of messages in $G \times G$, and a guessing function,
which maps a public key $h \in G$, a ciphertext in $G \times G$ and coins $r \in R$ to a bit.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.Adversary`, a structure declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#adversary).

## ElGamal eavesdropping experiment

Let $G$ be a commutative group, $g \in G$ and $q \ge 1$.
For an eavesdropping adversary $A$ with coins in a finite nonempty type $R$, the experiment draws
$x, y \in \mathbb{Z}/q$, coins $r \in R$ and a bit $b$ independently and uniformly. It sets the
public key $h = g^x$, lets $A$ choose messages $(m_0, m_1)$ from $h$ and $r$, and gives $A$ the
key $h$, the ElGamal ciphertext $(g^y, h^y m_b)$ and the coins $r$, where $m_b$ is $m_1$ if $b$
is true and $m_0$ otherwise; powers use the value of the exponent in $\{0, \dots, q - 1\}$. The
experiment outputs the distribution of the bit "the guess of $A$ equals $b$".

Formalized by `Cslib.Crypto.PublicKey.ElGamal.eavGame`, a definition declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#eav-game).

## Eavesdropping advantage against ElGamal

Let $G$ be a finite commutative group, $g \in G$
and $q \ge 1$. The eavesdropping advantage of an adversary $A$ with random coins in a finite
nonempty type $R$ is the real number $|p - 1/2|$, where $p$ is the probability that $A$ wins the
ElGamal eavesdropping experiment for $g$ with exponents in $\mathbb{Z}/q\mathbb{Z}$, that is,
guesses the challenge bit correctly.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.eavAdvantage`, a definition declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#eav-advantage).

## Real DDH experiment

Let $G$ be a finite commutative group, $g \in G$ and $q \ge 1$ a
natural number, and let $D$ be a distinguisher that maps three elements of $G$ and coins in a
finite nonempty type $S$ to a bit. The real DDH experiment draws $x, y \in \mathbb{Z}/q$ and coins
$s \in S$ independently and uniformly and outputs the distribution of the bit
$D(g^x, g^y, g^{xy}, s)$, where $xy$ is the product in $\mathbb{Z}/q$ and a power $g^a$ with
$a \in \mathbb{Z}/q$ means $g^{v(a)}$ for the representative $v(a) \in \{0, \dots, q - 1\}$
of $a$.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.ddhReal`, a definition declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#ddh-real).

## Random DDH experiment

Let $G$ be a finite commutative group, $g \in G$ and $q \ge 1$ a
natural number, and let $D$ be a distinguisher that maps three elements of $G$ and coins in a
finite nonempty type $S$ to a bit. The random DDH experiment draws $x, y, z \in \mathbb{Z}/q$ and
coins $s \in S$ independently and uniformly and outputs the distribution of the bit
$D(g^x, g^y, g^z, s)$, where a power $g^a$ with $a \in \mathbb{Z}/q$ means $g^{v(a)}$ for the
representative $v(a) \in \{0, \dots, q - 1\}$ of $a$.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.ddhRand`, a definition declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#ddh-rand).

## Advantage of a DDH distinguisher

Let $G$ be a finite commutative group, $g \in G$ and
$q \ge 1$, and let $D$ be a distinguisher that maps three elements of $G$ and coins in a finite
nonempty type $S$ to a bit. The DDH advantage of $D$ is the real number
$|p_{\mathrm{real}} - p_{\mathrm{rand}}|$, where $p_{\mathrm{real}}$ and $p_{\mathrm{rand}}$ are
the probabilities that $D$ outputs true in the real and in the random DDH experiment for $g$ with
exponents in $\mathbb{Z}/q\mathbb{Z}$.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.ddhAdvantage`, a definition declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#ddh-advantage).

## DDH distinguisher from an ElGamal eavesdropper

Let $G$ be a finite commutative group and
let $A$ be an eavesdropping adversary with coins in a finite nonempty type $R$. The distinguisher
built from $A$ takes three elements $X, Y, Z \in G$ and coins consisting of $r \in R$ and a bit
$b$. It lets $A$ choose messages $(m_0, m_1)$ from the public key $X$ and the coins $r$, gives $A$
the public key $X$, the ciphertext $(Y, Z m_b)$ and the coins $r$, where $m_b$ is $m_1$ if $b$ is
true and $m_0$ otherwise, and outputs true exactly when the guess of $A$ equals $b$.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.reduction`, a definition declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#reduction).

## ElGamal eavesdropping game equals the real DDH experiment of the reduction

Let $G$ be a
commutative group, $q \ge 1$ a natural number and $g \in G$ with $g^q = 1$. For every
eavesdropping adversary $A$ with coins in a finite nonempty type $R$, the output distribution of
the ElGamal eavesdropping experiment for $A$ (exponents in $\mathbb{Z}/q$) equals the output
distribution of the real DDH experiment run with the distinguisher built from $A$ by the
reduction.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.eavGame_eq_ddhReal`, a theorem declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#eav-game-eq-ddh-real).

## The reduction is a fair coin on random DDH triples

Let $G$ be a finite commutative group
of order $q$ generated by $g$. For every eavesdropping adversary $A$ with random coins in a finite
nonempty type $R$, the DDH distinguisher obtained from $A$ by the reduction outputs true with
probability exactly $1/2$ in the random DDH experiment for $g$.

In that experiment the third input $g^z$, with $z$ uniform in $\mathbb{Z}/q\mathbb{Z}$, is a group
one-time pad on the challenge message.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.ddhRand_reduction_true`, a theorem declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#ddh-rand-reduction-true).

## ElGamal eavesdropping advantage equals a DDH advantage

Let $G$ be a finite commutative
group of order $q$ generated by $g$. For every eavesdropping adversary $A$ with random coins in a
finite nonempty type $R$, the eavesdropping advantage of $A$ against ElGamal equals the DDH
advantage of the distinguisher obtained from $A$ by the reduction.

This is the eavesdropping part of Katz and Lindell, Theorem 11.18 (ElGamal is secure if DDH is
hard), in exact, non-asymptotic form.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.eavAdvantage_eq_ddhAdvantage`, a theorem declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#eav-advantage-eq-ddh-advantage).

## DDH bounds transfer to ElGamal

Let $G$ be a finite commutative group of order $q$
generated by $g$, and let $A$ be an eavesdropping adversary with random coins in a finite nonempty
type $R$. For every real number $\varepsilon$, if the DDH advantage of the distinguisher obtained
from $A$ by the reduction is at most $\varepsilon$, then the eavesdropping advantage of $A$
against ElGamal is at most $\varepsilon$.

Formalized by `Cslib.Crypto.PublicKey.ElGamal.eavAdvantage_le`, a theorem declared in [CSLibExt/Crypto/PublicKey/ElGamal.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/PublicKey/ElGamal.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html#eav-advantage-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: ElGamal encryption](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/cryptography/public-key/elgamal-encryption)
