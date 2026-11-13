---
declaration: section
origin: cited
lean: NumberField.finite_ramified_primes, NumberField.isUnramifiedIn_mono, NumberField.IsUnramifiedIn.etale_localization, NumberField.IsUnramifiedIn.tensorProductLocalizationEquivIntegralClosure, Localization.semilocalizationToAtPrime, Localization.semilocalizationToAtPrime_mk'_eq_iff, NumberField.IsUnramifiedIn.normalizedTensorToCompositumAtPrime, NumberField.IsUnramifiedIn.normalizedTensorToCompositumAtPrime_equiv_tmul
statement: formalized
proof: formalized
---

# Ramification in extensions of number fields

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html).

## Only finitely many primes ramify in a number field extension

Only finitely many height-one primes of a number field ramify
in a number-field extension.

Formalized by `NumberField.finite_ramified_primes`, a theorem declared in [MathlibExt/NumberTheory/NumberField/FiniteRamification.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/FiniteRamification.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#finite-ramified-primes).

## Unramifiedness descends to smaller intermediate fields

Let $L$ be a number field, let
$E \subseteq F$ be intermediate fields of $L/\mathbb{Q}$, and let $\mathfrak{p}$ be an ideal of
$\mathbb{Z}$. If $\mathfrak{p}$ is unramified in $\mathcal{O}_F$, that is, every prime ideal of
$\mathcal{O}_F$ lying over $\mathfrak{p}$ is unramified over $\mathbb{Z}$, then $\mathfrak{p}$ is
unramified in $\mathcal{O}_E$.

## Sources

- ATLAS N390, Proposition 19.14.

Formalized by `NumberField.isUnramifiedIn_mono`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#is-unramified-in-mono).

## Localizing the ring of integers at an unramified prime gives an étale algebra

Let $K$ be
a number field with ring of integers $\mathcal{O}_K$, and let $p$ be a prime ideal of $\mathbb{Z}$
that is unramified in $\mathcal{O}_K$, that is, every prime ideal of $\mathcal{O}_K$ lying over $p$
is unramified over $\mathbb{Z}$. Let $S$ be the localization of $\mathcal{O}_K$ at the image of
the multiplicative set $\mathbb{Z} \setminus p$. Then $S$ is an étale algebra over the local ring
$\mathbb{Z}_{(p)}$.

The ring $S$ is semilocal: it keeps every prime of $\mathcal{O}_K$ above $p$ at once, rather than
the localization $(\mathcal{O}_K)_Q$ at a single such prime $Q$.

## Sources

- packages the primewise unramified hypothesis used in ATLAS N390, Proposition 19.14.

Formalized by `NumberField.IsUnramifiedIn.etale_localization`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#etale-localization).

## Normalization commutes with base change along an unramified prime

Let $E$ and $F$ be
number fields and let $\mathfrak p$ be a prime ideal of $\mathbb Z$ that is unramified in the ring
of integers $\mathcal O_F$. Write $R = \mathbb Z_{\mathfrak p}$ for the localization of $\mathbb Z$
at $\mathfrak p$, and for $K = E, F$ write $S_K$ for the localization of $\mathcal O_K$ at the
image of $\mathbb Z \setminus \mathfrak p$. Let $K_E$ be the fraction field of $\mathcal O_E$ and
let $\iota : S_E \to K_E$ be the canonical map. This is the isomorphism of $S_F$-algebras from
$S_F \otimes_R S_E$ onto the integral closure of $S_F$ in $S_F \otimes_R K_E$ that, for
$s \in S_F$ and $t \in S_E$, sends $s \otimes t$ to $s \otimes \iota(t)$.

It is obtained from the identification of $S_E$ with the integral closure of $R$ in $K_E$, using
that $S_F$ is étale over $R$.

Formalized by `NumberField.IsUnramifiedIn.tensorProductLocalizationEquivIntegralClosure`, a definition declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#tensor-product-localization-equiv-integr).

## Map from the localization away from a prime to the local ring at a prime above it

Let
$R \to S \to T$ be homomorphisms of commutative rings whose algebra structures form a scalar
tower, let $\mathfrak p$ be a prime ideal of $R$, and let $\mathfrak Q$ be a prime ideal of $T$
lying over $\mathfrak p$. Write $S_{\mathfrak p}$ for the localization of $S$ at the image of
$R \setminus \mathfrak p$. This is the homomorphism of $S$-algebras
$S_{\mathfrak p} \to T_{\mathfrak Q}$ extending the composite $S \to T \to T_{\mathfrak Q}$; it
exists because elements of $R \setminus \mathfrak p$ map outside $\mathfrak Q$, hence to units of
$T_{\mathfrak Q}$.

Formalized by `Localization.semilocalizationToAtPrime`, a definition declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#semilocalization-to-at-prime).

## Values of the localization-to-local-ring map on fractions

Let $R \to S \to T$ be
homomorphisms of commutative rings whose algebra structures form a scalar tower, let
$\mathfrak p$ be a prime ideal of $R$, and let $\mathfrak Q$ be a prime ideal of $T$ lying over
$\mathfrak p$. Write $S_{\mathfrak p}$ for the localization of $S$ at the image of
$R \setminus \mathfrak p$, and let $\varphi : S_{\mathfrak p} \to T_{\mathfrak Q}$ be the
$S$-algebra homomorphism extending the composite $S \to T \to T_{\mathfrak Q}$. For $x \in S$,
$y$ in the image of $R \setminus \mathfrak p$ in $S$, and $z \in T_{\mathfrak Q}$, we have
$\varphi(x/y) = z$ if and only if $x = yz$ in $T_{\mathfrak Q}$, where $x$ and $y$ stand for
their images under $S \to T \to T_{\mathfrak Q}$.

Formalized by `Localization.semilocalizationToAtPrime_mk'_eq_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#semilocalization-to-at-prime-mk-eq-iff).

## Map from the normalized tensor algebra to the local ring of the compositum

Let $E$ and
$F$ be intermediate fields of a number field $L$ over $\mathbb Q$, let $\mathfrak p$ be a prime
ideal of $\mathbb Z$ that is unramified in $\mathcal O_F$, and let $\mathfrak Q$ be a prime ideal of
the ring of integers $\mathcal O_{EF}$ of the compositum $EF$ of $E$ and $F$ in $L$ lying over
$\mathfrak p$. Write $R = \mathbb Z_{\mathfrak p}$ for the localization of $\mathbb Z$ at
$\mathfrak p$; for $K = E, F$ write $S_K$ for the localization of $\mathcal O_K$ at the image of
$\mathbb Z \setminus \mathfrak p$ and $\varphi_K : S_K \to (\mathcal O_{EF})_{\mathfrak Q}$ for the
map induced by the inclusion $\mathcal O_K \subseteq \mathcal O_{EF}$; and let $C$ be the integral
closure of $S_F$ in $S_F \otimes_R \operatorname{Frac}(\mathcal O_E)$. This is the $R$-algebra
homomorphism $C \to (\mathcal O_{EF})_{\mathfrak Q}$ obtained by composing the inverse of the
canonical isomorphism $S_F \otimes_R S_E \cong C$ with the map
$S_F \otimes_R S_E \to (\mathcal O_{EF})_{\mathfrak Q}$ that, for $s \in S_F$ and $t \in S_E$,
sends $s \otimes t$ to $\varphi_F(s) \varphi_E(t)$.

No claim is made that this map induces an isomorphism from a localization of $C$ onto
$(\mathcal O_{EF})_{\mathfrak Q}$.

Formalized by `NumberField.IsUnramifiedIn.normalizedTensorToCompositumAtPrime`, a definition declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#normalized-tensor-to-compositum-at-prime).

## The normalized tensor map on simple tensors

Let $L$ be a number field, let $E$ and $F$ be
intermediate fields of $L/\mathbb{Q}$ with compositum $EF$, let $p$ be a prime ideal of
$\mathbb{Z}$ that is unramified in $\mathcal{O}_F$, and let $Q$ be a prime ideal of
$\mathcal{O}_{EF}$ lying over $p$. Write $R = \mathbb{Z}_{(p)}$, let $S_F$ and $S_E$ be the
localizations of $\mathcal{O}_F$ and $\mathcal{O}_E$ at the image of $\mathbb{Z} \setminus p$, let
$C$ be the integral closure of $S_F$ in $S_F \otimes_R \operatorname{Frac}(\mathcal{O}_E)$, let
$T = (\mathcal{O}_{EF})_Q$, and let $g \colon C \to T$ be the normalized tensor map to the
compositum at $Q$. Let $e \colon S_F \otimes_R S_E \to C$ be the normalization isomorphism, and
let $f_F \colon S_F \to T$ and $f_E \colon S_E \to T$ be the maps induced by the inclusions of
$\mathcal{O}_F$ and $\mathcal{O}_E$ into $\mathcal{O}_{EF}$. Then for all $x \in S_F$ and
$y \in S_E$, we have $g(e(x \otimes y)) = f_F(x)\,f_E(y)$.

Formalized by `NumberField.IsUnramifiedIn.normalizedTensorToCompositumAtPrime_equiv_tmul`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#normalized-tensor-to-compositum-at-prime-2).

## The kernel of the normalized tensor map is prime

Let $L$ be a number field, let $E$ and
$F$ be intermediate fields of $L/\mathbb{Q}$ with compositum $EF$, let $p$ be a prime ideal of
$\mathbb{Z}$ that is unramified in $\mathcal{O}_F$, and let $Q$ be a prime ideal of
$\mathcal{O}_{EF}$ lying over $p$. Write $R = \mathbb{Z}_{(p)}$, let $S_F$ be the localization of
$\mathcal{O}_F$ at the image of $\mathbb{Z} \setminus p$, let $C$ be the integral closure of $S_F$
in $S_F \otimes_R \operatorname{Frac}(\mathcal{O}_E)$, and let
$g \colon C \to (\mathcal{O}_{EF})_Q$ be the normalized tensor map to the compositum at $Q$. Then
the kernel of $g$ is a prime ideal of $C$.

This holds because $(\mathcal{O}_{EF})_Q$ is an integral domain. The kernel of $g$ is in general
strictly smaller than the preimage under $g$ of the maximal ideal of the local ring
$(\mathcal{O}_{EF})_Q$, which is the prime of $C$ at which to localize.

Formalized by `NumberField.IsUnramifiedIn.normalizedTensorToCompositumAtPrime_ker_isPrime`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#normalized-tensor-to-compositum-at-prime-3).

## The contracted maximal prime of the normalized tensor algebra

Let $L$ be a number field,
let $E$ and $F$ be intermediate fields of $L/\mathbb{Q}$ with compositum $EF$, let $p$ be a prime
ideal of $\mathbb{Z}$ that is unramified in $\mathcal{O}_F$, and let $Q$ be a prime ideal of
$\mathcal{O}_{EF}$ lying over $p$. Write $R = \mathbb{Z}_{(p)}$, let $S_F$ be the localization of
$\mathcal{O}_F$ at the image of $\mathbb{Z} \setminus p$, let $C$ be the integral closure of $S_F$
in $S_F \otimes_R \operatorname{Frac}(\mathcal{O}_E)$, let $T = (\mathcal{O}_{EF})_Q$ be the
localization of $\mathcal{O}_{EF}$ at $Q$, and let $g \colon C \to T$ be the normalized tensor map
to the compositum at $Q$. The contracted maximal prime is the ideal $g^{-1}(\mathfrak{m}_T)$ of
$C$, where $\mathfrak{m}_T$ is the maximal ideal of the local ring $T$.

It contains the kernel of $g$, and is in general strictly larger. It is intended as the prime of
$C$ at which to localize in order to recover the local factor $T$.

## Sources

- ATLAS N390, Proposition 19.14.

Formalized by `NumberField.IsUnramifiedIn.normalizedTensorCompositumPrime`, a definition declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#normalized-tensor-compositum-prime).

## The contracted maximal prime is prime

Let $L$ be a number field, let $E$ and $F$ be
intermediate fields of $L/\mathbb{Q}$ with compositum $EF$, let $p$ be a prime ideal of
$\mathbb{Z}$ that is unramified in $\mathcal{O}_F$, and let $Q$ be a prime ideal of
$\mathcal{O}_{EF}$ lying over $p$. Then the contracted maximal prime of the normalized tensor
algebra at $Q$ is a prime ideal.

It is the preimage of the maximal ideal of the local ring $(\mathcal{O}_{EF})_Q$, which is
prime.

Formalized by `NumberField.IsUnramifiedIn.normalizedTensorCompositumPrime_isPrime`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#normalized-tensor-compositum-prime-is-pr).

## Membership in the contracted maximal prime

Let $L$ be a number field, let $E$ and $F$ be
intermediate fields of $L/\mathbb{Q}$ with compositum $EF$, let $p$ be a prime ideal of
$\mathbb{Z}$ that is unramified in $\mathcal{O}_F$, and let $Q$ be a prime ideal of
$\mathcal{O}_{EF}$ lying over $p$. Write $R = \mathbb{Z}_{(p)}$, let $S_F$ be the localization of
$\mathcal{O}_F$ at the image of $\mathbb{Z} \setminus p$, let $C$ be the integral closure of $S_F$
in $S_F \otimes_R \operatorname{Frac}(\mathcal{O}_E)$, let $T = (\mathcal{O}_{EF})_Q$, and let
$g \colon C \to T$ be the normalized tensor map to the compositum at $Q$. An element $x \in C$
lies in the contracted maximal prime if and only if $g(x)$ lies in the maximal ideal of the local
ring $T$.

Formalized by `NumberField.IsUnramifiedIn.normalizedTensorCompositumPrime_mem_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#normalized-tensor-compositum-prime-mem-i).

## The kernel lies in the contracted maximal ideal

Let $E$ and $F$ be intermediate fields of
a number field $L$ over $\mathbb Q$, let $\mathfrak p$ be a prime ideal of $\mathbb Z$ that is
unramified in $\mathcal O_F$, and let $\mathfrak Q$ be a prime ideal of the ring of integers
$\mathcal O_{EF}$ of the compositum $EF$ of $E$ and $F$ in $L$ lying over $\mathfrak p$. Write
$R = \mathbb Z_{\mathfrak p}$ for the localization of $\mathbb Z$ at $\mathfrak p$; for
$K = E, F$ let $S_K$ be the localization of $\mathcal O_K$ at the image of
$\mathbb Z \setminus \mathfrak p$ and let $\varphi_K : S_K \to (\mathcal O_{EF})_{\mathfrak Q}$ be
the map induced by the inclusion $\mathcal O_K \subseteq \mathcal O_{EF}$; let $C$ be the integral
closure of $S_F$ in $S_F \otimes_R \operatorname{Frac}(\mathcal O_E)$; and let
$g : C \to (\mathcal O_{EF})_{\mathfrak Q}$ be the $R$-algebra homomorphism that, for $s \in S_F$
and $t \in S_E$, sends the image of $s \otimes t$ under the canonical isomorphism
$S_F \otimes_R S_E \cong C$ to $\varphi_F(s) \varphi_E(t)$. Then the kernel of $g$ is contained in
the preimage under $g$ of the maximal ideal of $(\mathcal O_{EF})_{\mathfrak Q}$.

Formalized by `NumberField.IsUnramifiedIn.normalizedTensorToCompositumAtPrime_ker_le`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#normalized-tensor-to-compositum-at-prime-4).

## The localization map to the compositum at a prime

Let $L$ be a number field, let $E$ and
$F$ be intermediate fields of $L/\mathbb{Q}$ with compositum $EF$, let $p$ be a prime ideal of
$\mathbb{Z}$ that is unramified in $\mathcal{O}_F$, and let $Q$ be a prime ideal of
$\mathcal{O}_{EF}$ lying over $p$. Write $R = \mathbb{Z}_{(p)}$, let $S_F$ be the localization of
$\mathcal{O}_F$ at the image of $\mathbb{Z} \setminus p$, let $C$ be the integral closure of $S_F$
in $S_F \otimes_R \operatorname{Frac}(\mathcal{O}_E)$, let $T = (\mathcal{O}_{EF})_Q$, let
$g \colon C \to T$ be the normalized tensor map to the compositum at $Q$, and let $\mathfrak{q}$
be the contracted maximal prime of $C$. Since $g$ sends every element of $C \setminus \mathfrak{q}$
outside the maximal ideal of the local ring $T$, hence to a unit, $g$ induces by the universal
property of localization a ring homomorphism $C_{\mathfrak{q}} \to T$, sending $x/s$ to
$g(x)\,g(s)^{-1}$.

Formalized by `NumberField.IsUnramifiedIn.normalizedTensorLocalizationToCompositumAtPrime`, a definition declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#normalized-tensor-localization-to-compos).

## The localization map restricts to the normalized tensor map

Let $L$ be a number field,
let $E$ and $F$ be intermediate fields of $L/\mathbb{Q}$ with compositum $EF$, let $p$ be a prime
ideal of $\mathbb{Z}$ that is unramified in $\mathcal{O}_F$, and let $Q$ be a prime ideal of
$\mathcal{O}_{EF}$ lying over $p$. Write $R = \mathbb{Z}_{(p)}$, let $S_F$ be the localization of
$\mathcal{O}_F$ at the image of $\mathbb{Z} \setminus p$, let $C$ be the integral closure of $S_F$
in $S_F \otimes_R \operatorname{Frac}(\mathcal{O}_E)$, let $T = (\mathcal{O}_{EF})_Q$, let
$g \colon C \to T$ be the normalized tensor map to the compositum at $Q$, let $\mathfrak{q}$ be the
contracted maximal prime of $C$, and let $\varphi \colon C_{\mathfrak{q}} \to T$ be the
localization map to the compositum at $Q$. Then for every $x \in C$, $\varphi$ sends the image of
$x$ in $C_{\mathfrak{q}}$ to $g(x)$.

Formalized by `NumberField.IsUnramifiedIn.normalizedTensorLocalizationToCompositumAtPrime_algebraMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#normalized-tensor-localization-to-compos-2).

## Value of the localization map on fractions

Let $L$ be a number field, let $E$ and $F$ be
intermediate fields of $L/\mathbb{Q}$ with compositum $EF$, let $p$ be a prime ideal of
$\mathbb{Z}$ that is unramified in $\mathcal{O}_F$, and let $Q$ be a prime ideal of
$\mathcal{O}_{EF}$ lying over $p$. Write $R = \mathbb{Z}_{(p)}$, let $S_F$ be the localization of
$\mathcal{O}_F$ at the image of $\mathbb{Z} \setminus p$, let $C$ be the integral closure of $S_F$
in $S_F \otimes_R \operatorname{Frac}(\mathcal{O}_E)$, let $T = (\mathcal{O}_{EF})_Q$, let
$g \colon C \to T$ be the normalized tensor map to the compositum at $Q$, let $\mathfrak{q}$ be the
contracted maximal prime of $C$, and let $\varphi \colon C_{\mathfrak{q}} \to T$ be the
localization map to the compositum at $Q$. Then for all $x \in C$, $s \in C \setminus \mathfrak{q}$
and $v \in T$, we have $\varphi(x/s) = v$ if and only if $g(x) = g(s)\,v$.

Formalized by `NumberField.IsUnramifiedIn.normalizedTensorLocalizationToCompositumAtPrime_mk'_spec`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Unramified.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Unramified.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html#normalized-tensor-localization-to-compos-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramification in extensions of number fields](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/ramification-in-extensions-of-number-fields)
