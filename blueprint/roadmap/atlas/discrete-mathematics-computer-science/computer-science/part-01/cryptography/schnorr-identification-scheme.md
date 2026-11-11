---
declaration: section
origin: cited
lean: Cslib.Crypto.Identification.Schnorr.Accepts, Cslib.Crypto.Identification.Schnorr.respond, Cslib.Crypto.Identification.Schnorr.accepts_honest, Cslib.Crypto.Identification.Schnorr.extract, Cslib.Crypto.Identification.Schnorr.extract_spec, Cslib.Crypto.Identification.Schnorr.honestTranscript, Cslib.Crypto.Identification.Schnorr.simTranscript, Cslib.Crypto.Identification.Schnorr.transcript
statement: formalized
proof: formalized
---

# Schnorr identification scheme

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html).

## Schnorr verifier's acceptance condition

Let $G$ be a commutative group, $q$ a natural
number and $g, y \in G$ (the base and the public key); for $h \in G$ and $a \in \mathbb{Z}/q$
write $h^a$ for $h^{\bar a}$, where $\bar a$ is the representative of $a$ in
$\{0, \dots, q - 1\}$ (and $\bar a = |a|$ when $q = 0$, so that $\mathbb{Z}/q = \mathbb{Z}$).
The verifier accepts a transcript $(I, r, s)$ with $I \in G$ and $r, s \in \mathbb{Z}/q$ when
$g^s (y^r)^{-1} = I$.

Formalized by `Cslib.Crypto.Identification.Schnorr.Accepts`, a definition declared in [CSLibExt/Crypto/Identification/Schnorr.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Identification/Schnorr.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html#accepts).

## Schnorr prover's response

Let $q$ be a natural number. For a secret key $x$, prover
randomness $k$ and challenge $r$, all in $\mathbb{Z}/q$, the prover's answer is
$s = rx + k \in \mathbb{Z}/q$.

Formalized by `Cslib.Crypto.Identification.Schnorr.respond`, a definition declared in [CSLibExt/Crypto/Identification/Schnorr.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Identification/Schnorr.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html#respond).

## Completeness of the Schnorr identification scheme

Let $G$ be a commutative group,
$q \ge 1$ a natural number and $g \in G$ with $g^q = 1$; for $h \in G$ and $a \in \mathbb{Z}/q$
write $h^a$ for $h^{\bar a}$, where $\bar a \in \{0, \dots, q - 1\}$ is the representative
of $a$. For all $x, k, r \in \mathbb{Z}/q$, with public key $y = g^x$, the honest transcript
$(g^k, r, rx + k)$ is accepted, that is, $g^{rx + k} (y^r)^{-1} = g^k$.

Formalized by `Cslib.Crypto.Identification.Schnorr.accepts_honest`, a theorem declared in [CSLibExt/Crypto/Identification/Schnorr.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Identification/Schnorr.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html#accepts-honest).

## Schnorr knowledge extractor

Let $q$ be a natural number. For
$r, s, r', s' \in \mathbb{Z}/q$ (the challenges and answers of two transcripts), the extracted
exponent is $(s - s')(r - r')^{-1} \in \mathbb{Z}/q$, where $u^{-1}$ is the inverse of $u$ in
$\mathbb{Z}/q$ when $u$ is a unit (and, otherwise, a conventional element of $\mathbb{Z}/q$
depending on $u$). For $q$ prime and $r \ne r'$ it is $(s - s')/(r - r')$.

Formalized by `Cslib.Crypto.Identification.Schnorr.extract`, a definition declared in [CSLibExt/Crypto/Identification/Schnorr.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Identification/Schnorr.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html#extract).

## Special soundness

Let $G$ be a commutative group, $q$ a prime and $g, y \in G$ with
$g^q = 1$ and $y^q = 1$; for $h \in G$ and $a \in \mathbb{Z}/q$ write $h^a$ for $h^{\bar a}$,
where $\bar a \in \{0, \dots, q - 1\}$ is the representative of $a$. Let $I \in G$ and
$r, s, r', s' \in \mathbb{Z}/q$ with $r \ne r'$, and suppose both transcripts $(I, r, s)$ and
$(I, r', s')$ are accepted, that is, $g^s (y^r)^{-1} = I$ and $g^{s'} (y^{r'})^{-1} = I$. Then
the extracted exponent $e = (s - s')(r - r')^{-1}$ is a discrete logarithm of $y$: $g^e = y$.

Formalized by `Cslib.Crypto.Identification.Schnorr.extract_spec`, a theorem declared in [CSLibExt/Crypto/Identification/Schnorr.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Identification/Schnorr.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html#extract-spec).

## Honest Schnorr transcript

Let $G$ be a commutative group, $q \ge 1$ and $g \in G$; for
$a \in \mathbb{Z}/q$ write $g^a$ for $g^{\bar a}$, where $\bar a \in \{0, \dots, q - 1\}$ is the
representative of $a$. For a secret key $x$, prover randomness $k$ and challenge $r$, all in
$\mathbb{Z}/q$, the honest transcript is the element $(g^k, r, rx + k)$ of
$G \times \mathbb{Z}/q \times \mathbb{Z}/q$.

Formalized by `Cslib.Crypto.Identification.Schnorr.honestTranscript`, a definition declared in [CSLibExt/Crypto/Identification/Schnorr.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Identification/Schnorr.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html#honest-transcript).

## Simulated Schnorr transcript

Let $G$ be a commutative group, $q \ge 1$ and $g, y \in G$;
for $h \in G$ and $a \in \mathbb{Z}/q$ write $h^a$ for $h^{\bar a}$, where
$\bar a \in \{0, \dots, q - 1\}$ is the representative of $a$. For a challenge $r$ and an answer
$s$ in $\mathbb{Z}/q$, the simulated transcript is the element $(g^s (y^r)^{-1}, r, s)$ of
$G \times \mathbb{Z}/q \times \mathbb{Z}/q$.

Formalized by `Cslib.Crypto.Identification.Schnorr.simTranscript`, a definition declared in [CSLibExt/Crypto/Identification/Schnorr.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Identification/Schnorr.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html#sim-transcript).

## Distribution of honest Schnorr transcripts

Let $G$ be a commutative group, $q \ge 1$ and
$g \in G$; for $a \in \mathbb{Z}/q$ write $g^a$ for $g^{\bar a}$, where
$\bar a \in \{0, \dots, q - 1\}$ is the representative of $a$. For a secret key
$x \in \mathbb{Z}/q$, this is the law of the honest transcript $(g^k, r, rx + k)$ when $(k, r)$ is
uniform on $\mathbb{Z}/q \times \mathbb{Z}/q$.

Formalized by `Cslib.Crypto.Identification.Schnorr.transcript`, a definition declared in [CSLibExt/Crypto/Identification/Schnorr.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Identification/Schnorr.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html#transcript).

## Schnorr simulator

Let $G$ be a commutative group, $q \ge 1$ and $g, y \in G$; for
$h \in G$ and $a \in \mathbb{Z}/q$ write $h^a$ for $h^{\bar a}$, where
$\bar a \in \{0, \dots, q - 1\}$ is the representative of $a$. The simulator's distribution is
the law of the simulated transcript $(g^s (y^r)^{-1}, r, s)$ when $(r, s)$ is uniform on
$\mathbb{Z}/q \times \mathbb{Z}/q$; it uses only $g$ and the public key $y$.

Formalized by `Cslib.Crypto.Identification.Schnorr.simulate`, a definition declared in [CSLibExt/Crypto/Identification/Schnorr.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Identification/Schnorr.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html#simulate).

## Perfect honest-verifier zero knowledge

Let $G$ be a commutative group, $q \ge 1$ and
$g \in G$ with $g^q = 1$; for $h \in G$ and $a \in \mathbb{Z}/q$ write $h^a$ for $h^{\bar a}$,
where $\bar a \in \{0, \dots, q - 1\}$ is the representative of $a$. For every secret key
$x \in \mathbb{Z}/q$, with public key $y = g^x$, the honest transcript $(g^k, r, rx + k)$ with
$(k, r)$ uniform on $\mathbb{Z}/q \times \mathbb{Z}/q$ has the same distribution as the
simulated transcript $(g^s (y^r)^{-1}, r, s)$ with $(r, s)$ uniform on
$\mathbb{Z}/q \times \mathbb{Z}/q$.

Formalized by `Cslib.Crypto.Identification.Schnorr.transcript_eq_simulate`, a theorem declared in [CSLibExt/Crypto/Identification/Schnorr.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Identification/Schnorr.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html#transcript-eq-simulate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schnorr identification scheme](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/schnorr-identification-scheme/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/cryptography/schnorr-identification-scheme)
