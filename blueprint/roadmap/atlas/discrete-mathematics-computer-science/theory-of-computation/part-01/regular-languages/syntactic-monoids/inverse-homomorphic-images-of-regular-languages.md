---
declaration: section
origin: cited
lean: Cslib.Language.alphabetPreimage, Cslib.Language.alphabetPreimageMorphism, Cslib.Language.recognizes_alphabetPreimageMorphism, Cslib.Language.syntacticRel_alphabetPreimage_of_map, Cslib.Language.alphabetPreimageMorphism_ker_le, Cslib.Language.alphabetPreimageToSyntactic, Cslib.Language.finite_syntacticMonoid_alphabetPreimage, Cslib.Language.IsRegular.alphabetPreimage
statement: formalized
proof: formalized
---

# Inverse homomorphic images of regular languages

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html).

## Alphabet preimage

Let $f \colon \Sigma \to \Gamma$ be a map between alphabets and $L$ a
language over $\Gamma$. The alphabet preimage of $L$ under $f$ is the language over $\Sigma$
consisting of the words $a_1 a_2 \cdots a_n$ such that $f(a_1) f(a_2) \cdots f(a_n) \in L$.

Formalized by `Cslib.Language.alphabetPreimage`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Morphisms.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Morphisms.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#alphabet-preimage).

## Alphabet preimage morphism

Let $f \colon \Sigma \to \Gamma$ be a map between alphabets
and $L$ a language over $\Gamma$. The alphabet preimage morphism of $f$ and $L$ is the monoid
morphism from the free monoid $\Sigma^*$ to the syntactic monoid of $L$ that sends a word $w$ to
the syntactic class of $f^*(w)$, the word obtained by applying $f$ to each letter of $w$. It is
the composite of the letterwise map $f^* \colon \Sigma^* \to \Gamma^*$ with the syntactic
morphism of $L$.

Formalized by `Cslib.Language.alphabetPreimageMorphism`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Morphisms.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Morphisms.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#alphabet-preimage-morphism).

## The alphabet preimage morphism recognizes the alphabet preimage

Let
$f \colon \Sigma \to \Gamma$ be a map between alphabets and $L$ a language over $\Gamma$. Write
$f^*(w)$ for the word obtained by applying $f$ to each letter of a word $w$, $[u]_L$ for the
class of a word $u$ in the syntactic monoid $M(L)$ of $L$, $A_L \subseteq M(L)$ for the
accepting set of classes of words in $L$, and $\varphi \colon \Sigma^* \to M(L)$ for the alphabet
preimage morphism $w \mapsto [f^*(w)]_L$. Then $\varphi$ recognizes the alphabet preimage
$\{w \in \Sigma^* \mid f^*(w) \in L\}$ through $A_L$: for every word $w \in \Sigma^*$, we have
$f^*(w) \in L$ if and only if $\varphi(w) \in A_L$.

Formalized by `Cslib.Language.recognizes_alphabetPreimageMorphism`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Morphisms.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Morphisms.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#recognizes-alphabet-preimage-morphism).

## Syntactic equivalence pulls back along an alphabet map

Let $f \colon \Sigma \to \Gamma$
be a map between alphabets, $L$ a language over $\Gamma$, and $K$ the alphabet preimage
$\{w \in \Sigma^* \mid f^*(w) \in L\}$, where $f^*(w)$ is the word obtained by applying $f$ to
each letter of $w$. If $x, y \in \Sigma^*$ are words such that $f^*(x)$ and $f^*(y)$ are
syntactically equivalent for $L$, then $x$ and $y$ are syntactically equivalent for $K$.

Formalized by `Cslib.Language.syntacticRel_alphabetPreimage_of_map`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Morphisms.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Morphisms.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#syntactic-rel-alphabet-preimage-of-map).

## The alphabet preimage morphism refines the preimage's syntactic congruence

Let
$f \colon \Sigma \to \Gamma$ be a map between alphabets, $L$ a language over $\Gamma$ with
syntactic monoid $M(L)$, and $\varphi \colon \Sigma^* \to M(L)$ the alphabet preimage morphism,
which sends a word $w$ to the class in $M(L)$ of the word $f^*(w)$ obtained by applying $f$ to
each letter of $w$. If two words $x, y \in \Sigma^*$ satisfy $\varphi(x) = \varphi(y)$, then $x$
and $y$ are syntactically congruent for the alphabet preimage
$\{w \in \Sigma^* \mid f^*(w) \in L\}$. In other words, the kernel congruence of $\varphi$ is
contained in the syntactic congruence of the alphabet preimage.

Formalized by `Cslib.Language.alphabetPreimageMorphism_ker_le`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Morphisms.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Morphisms.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#alphabet-preimage-morphism-ker-le).

## Division map for the syntactic monoid of an alphabet preimage

Let
$f \colon \Sigma \to \Gamma$ be a map between alphabets and $L$ a language over $\Gamma$. Write
$f^*(w)$ for the word obtained by applying $f$ to each letter of a word $w$, $[u]_L$ for the
class of a word $u$ in the syntactic monoid $M(L)$ of $L$, $K$ for the alphabet preimage
$\{w \in \Sigma^* \mid f^*(w) \in L\}$, and $\varphi \colon \Sigma^* \to M(L)$ for the alphabet
preimage morphism $w \mapsto [f^*(w)]_L$. This is the monoid morphism from the submonoid
$\varphi(\Sigma^*)$ of $M(L)$ to the syntactic monoid $M(K)$ that sends $\varphi(w)$ to $[w]_K$;
it is well defined because $\varphi(x) = \varphi(y)$ implies $[x]_K = [y]_K$.

This morphism is surjective, so $M(K)$ is a quotient of a submonoid of $M(L)$.

Formalized by `Cslib.Language.alphabetPreimageToSyntactic`, a definition declared in [CSLibExt/Computability/Languages/Congruences/Morphisms.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Morphisms.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#alphabet-preimage-to-syntactic).

## Alphabet preimages preserve finiteness of the syntactic monoid

Let
$f \colon \Sigma \to \Gamma$ be a map between alphabets and $L$ a language over $\Gamma$ whose
syntactic monoid is finite. Then the syntactic monoid of the alphabet preimage
$\{w \in \Sigma^* \mid f^*(w) \in L\}$ is finite, where $f^*(w)$ is the word obtained by applying
$f$ to each letter of $w$.

Formalized by `Cslib.Language.finite_syntacticMonoid_alphabetPreimage`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Morphisms.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Morphisms.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#finite-syntactic-monoid-alphabet-preimag).

## Regular languages are closed under alphabet preimages

Let $f \colon \Sigma \to \Gamma$
be a map between alphabets. If $L$ is a regular language over $\Gamma$, then its alphabet
preimage $\{w \in \Sigma^* \mid f^*(w) \in L\}$ is regular, where $f^*(w)$ is the word obtained
by applying $f$ to each letter of $w$.

Formalized by `Cslib.Language.IsRegular.alphabetPreimage`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Morphisms.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Morphisms.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#alphabet-preimage-2).

## Renaming letters by a bijection preserves and reflects regularity

Let
$e \colon \Sigma \to \Gamma$ be a bijection between alphabets and $L$ a language over $\Gamma$.
The alphabet preimage $\{w \in \Sigma^* \mid e^*(w) \in L\}$, where $e^*(w)$ is the word
obtained by applying $e$ to each letter of $w$, is regular if and only if $L$ is regular.

Formalized by `Cslib.Language.isRegular_alphabetPreimage_equiv_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Morphisms.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Morphisms.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#is-regular-alphabet-preimage-equiv-iff).

## Finiteness of the syntactic monoid is invariant under renaming letters

Let
$e \colon \Sigma \to \Gamma$ be a bijection between alphabets and $L$ a language over $\Gamma$.
The syntactic monoid of the alphabet preimage $\{w \in \Sigma^* \mid e^*(w) \in L\}$, where
$e^*(w)$ is the word obtained by applying $e$ to each letter of $w$, is finite if and only if
the syntactic monoid of $L$ is finite.

Formalized by `Cslib.Language.finite_syntacticMonoid_alphabetPreimage_equiv_iff`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/Morphisms.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/Morphisms.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#finite-syntactic-monoid-alphabet-preimag-2).

## Inverse image under a word morphism

Let $\Sigma$ and $\Gamma$ be alphabets,
$h \colon \Sigma^* \to \Gamma^*$ a monoid morphism between their free monoids of words, and $L$ a
language over $\Gamma$. The inverse image of $L$ under $h$ is the language
$h^{-1}(L) = \{w \in \Sigma^* \mid h(w) \in L\}$ over $\Sigma$.

Formalized by `Cslib.Language.wordMorphismPreimage`, a definition declared in [CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#word-morphism-preimage).

## Word morphisms act letter by letter

Let $h \colon \Sigma^* \to \Gamma^*$ be a monoid
morphism between free monoids. For every word $a_1 a_2 \cdots a_n \in \Sigma^*$ (including the
empty word, $n = 0$), we have $h(a_1 a_2 \cdots a_n) = h(a_1) h(a_2) \cdots h(a_n)$, the
concatenation of the images of its letters.

Formalized by `Cslib.Language.toList_wordMorphism_ofList`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#to-list-word-morphism-of-list).

## Letterwise description of the inverse image under a word morphism

Let
$h \colon \Sigma^* \to \Gamma^*$ be a monoid morphism between free monoids and $L$ a language over
$\Gamma$. The inverse image $h^{-1}(L) = \{w \in \Sigma^* \mid h(w) \in L\}$ consists exactly of
the words $a_1 a_2 \cdots a_n \in \Sigma^*$ such that the concatenation
$h(a_1) h(a_2) \cdots h(a_n)$ of the images of their letters lies in $L$.

Formalized by `Cslib.Language.wordMorphismPreimage_eq_flatten`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#word-morphism-preimage-eq-flatten).

## Recognizing morphism of an inverse image

Let $h \colon \Sigma^* \to \Gamma^*$ be a monoid
morphism between free monoids and $L$ a language over $\Gamma$ with syntactic monoid $M(L)$. The
recognizing morphism of $h$ and $L$ is the monoid morphism $\Sigma^* \to M(L)$ that sends a word
$w$ to the syntactic class $[h(w)]_L$ of $h(w)$; it is the composite of $h$ with the syntactic
morphism of $L$.

Formalized by `Cslib.Language.wordMorphismRecognizer`, a definition declared in [CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#word-morphism-recognizer).

## Syntactic equivalence pulls back along a word morphism

Let
$h \colon \Sigma^* \to \Gamma^*$ be a monoid morphism between free monoids, $L$ a language over
$\Gamma$, and $K = h^{-1}(L) = \{w \in \Sigma^* \mid h(w) \in L\}$ its inverse image. If
$x, y \in \Sigma^*$ are words such that $h(x)$ and $h(y)$ are syntactically equivalent for $L$,
then $x$ and $y$ are syntactically equivalent for $K$.

Formalized by `Cslib.Language.syntacticRel_wordMorphismPreimage_of_map`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#syntactic-rel-word-morphism-preimage-of).

## Division map for the syntactic monoid of an inverse image

Let
$h \colon \Sigma^* \to \Gamma^*$ be a monoid morphism between free monoids and $L$ a language over
$\Gamma$. Write $[u]_L$ for the class of a word $u$ in the syntactic monoid $M(L)$ of $L$, $K$ for
the inverse image $h^{-1}(L) = \{w \in \Sigma^* \mid h(w) \in L\}$, and
$\varphi \colon \Sigma^* \to M(L)$ for the recognizing morphism $w \mapsto [h(w)]_L$. This is the
monoid morphism from the submonoid $\varphi(\Sigma^*)$ of $M(L)$ to the syntactic monoid $M(K)$
that sends $\varphi(w)$ to $[w]_K$; it is well defined because $\varphi(x) = \varphi(y)$ implies
$[x]_K = [y]_K$.

This morphism is surjective, so $M(K)$ is a quotient of a submonoid of $M(L)$.

Formalized by `Cslib.Language.wordMorphismPreimageToSyntactic`, a definition declared in [CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#word-morphism-preimage-to-syntactic).

## Inverse images under word morphisms preserve finiteness of the syntactic monoid

Let
$h \colon \Sigma^* \to \Gamma^*$ be a monoid morphism between free monoids and $L$ a language over
$\Gamma$ whose syntactic monoid is finite. Then the syntactic monoid of the inverse image
$h^{-1}(L) = \{w \in \Sigma^* \mid h(w) \in L\}$ is finite.

Formalized by `Cslib.Language.finite_syntacticMonoid_wordMorphismPreimage`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#finite-syntactic-monoid-word-morphism-pr).

## Regular languages are closed under inverse word morphisms

Let
$h \colon \Sigma^* \to \Gamma^*$ be a monoid morphism between free monoids. If $L$ is a regular
language over $\Gamma$, then its inverse image $h^{-1}(L) = \{w \in \Sigma^* \mid h(w) \in L\}$ is
regular.

Formalized by `Cslib.Language.IsRegular.wordMorphismPreimage`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#word-morphism-preimage-2).

## Alphabet preimages are inverse images under word morphisms

Let
$f \colon \Sigma \to \Gamma$ be a map between alphabets, $f^* \colon \Sigma^* \to \Gamma^*$ the
monoid morphism that applies $f$ to each letter of a word, and $L$ a language over $\Gamma$. Then
the alphabet preimage of $L$ under $f$ equals the inverse image
$(f^*)^{-1}(L) = \{w \in \Sigma^* \mid f^*(w) \in L\}$ of $L$ under $f^*$.

Formalized by `Cslib.Language.alphabetPreimage_eq_wordMorphismPreimage`, a theorem declared in [CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/Congruences/WordMorphisms.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html#alphabet-preimage-eq-word-morphism-preim).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inverse homomorphic images of regular languages](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/regular-languages/syntactic-monoids/inverse-homomorphic-images-of-regular-languages)
