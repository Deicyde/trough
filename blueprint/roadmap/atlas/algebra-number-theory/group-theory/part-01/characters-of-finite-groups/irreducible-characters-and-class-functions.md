---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ClassFunctionWanted.IsClassFunction, MathlibExt.GroupTheory.ClassFunctionWanted.classFunctions, MathlibExt.GroupTheory.ClassFunctionWanted.character_isClassFunction, MathlibExt.GroupTheory.ClassFunctionWanted.IsClassFunction.eq_of_isConj, MathlibExt.GroupTheory.ClassFunctionWanted.isClassFunction_iff_factor_conjClasses, MathlibExt.GroupTheory.ClassFunctionWanted.classFunctionsEquivConjClasses, MathlibExt.GroupTheory.ClassFunctionWanted.classFunctionsEquivConjClasses_apply_mk, MathlibExt.GroupTheory.ClassFunctionWanted.classFunctionsEquivConjClasses_symm_apply
statement: formalized
proof: formalized
---

# Irreducible characters and class functions

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html).

## Class functions on a group

Let $G$ be a group and $k$ a set. A function
$f : G \to k$ is a class function when it is constant on conjugacy classes, that is,
$f(h g h^{-1}) = f(g)$ for all $g, h \in G$.

Formalized by `MathlibExt.GroupTheory.ClassFunctionWanted.IsClassFunction`, a definition declared in [MathlibExt/GroupTheory/ClassFunction.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassFunction.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#is-class-function).

## The space of class functions

Let $G$ be a group and $k$ a field. The space of
class functions $G \to k$ is the $k$-linear subspace of the vector space of all functions
$G \to k$, under pointwise addition and scalar multiplication, consisting of the class
functions.

Formalized by `MathlibExt.GroupTheory.ClassFunctionWanted.classFunctions`, a definition declared in [MathlibExt/GroupTheory/ClassFunction.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassFunction.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#class-functions).

## Characters are class functions

Let $G$ be a group and $k$ a field. For every
finite-dimensional representation $V$ of $G$ over $k$, the character of $V$, the function
sending $g \in G$ to the trace of the linear map by which $g$ acts on $V$, is a class
function on $G$.

## Sources

- J.-P. Serre, Linear Representations of Finite Groups, GTM 42, §2.1 (the character is constant on conjugacy classes).

Formalized by `MathlibExt.GroupTheory.ClassFunctionWanted.character_isClassFunction`, a theorem declared in [MathlibExt/GroupTheory/ClassFunction.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassFunction.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#character-is-class-function).

## Class functions agree on conjugate elements

Let $G$ be a group and let
$f : G \to k$ be a class function with values in a set $k$. If $x, y \in G$ are conjugate,
then $f(x) = f(y)$.

Formalized by `MathlibExt.GroupTheory.ClassFunctionWanted.IsClassFunction.eq_of_isConj`, a theorem declared in [MathlibExt/GroupTheory/ClassFunction.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassFunction.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#eq-of-is-conj).

## Class functions factor through conjugacy classes

Let $G$ be a group and $k$ a set,
and write $[x]$ for the conjugacy class of $x \in G$. A function $f : G \to k$ is a class
function if and only if there is a function $q$ from the set of conjugacy classes of $G$
to $k$ such that $f(x) = q([x])$ for all $x \in G$.

Proof: A class function is constant on each conjugacy class, so it descends to a function
on conjugacy classes. Conversely, if $f(x) = q([x])$ for all $x \in G$, then for all
$g, h \in G$ we have $f(h g h^{-1}) = q([h g h^{-1}]) = q([g]) = f(g)$, because
$h g h^{-1}$ and $g$ are conjugate.

## Sources

- J.-P. Serre, Linear Representations of Finite Groups, GTM 42, §2 (class functions as functions on conjugacy classes).

Formalized by `MathlibExt.GroupTheory.ClassFunctionWanted.isClassFunction_iff_factor_conjClasses`, a theorem declared in [MathlibExt/GroupTheory/ClassFunction.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassFunction.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#is-class-function-iff-factor-conj-classe).

## Class functions as functions on conjugacy classes

Let $G$ be a group and $k$ a
field, and write $[x]$ for the conjugacy class of $x \in G$. This is the $k$-linear
isomorphism from the space of class functions $G \to k$ to the vector space of all
functions from the set of conjugacy classes of $G$ to $k$ that sends a class function $f$
to the function $[x] \mapsto f(x)$; its inverse sends a function $q$ on conjugacy classes
to the class function $x \mapsto q([x])$.

Formalized by `MathlibExt.GroupTheory.ClassFunctionWanted.classFunctionsEquivConjClasses`, a definition declared in [MathlibExt/GroupTheory/ClassFunction.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassFunction.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#class-functions-equiv-conj-classes).

## Evaluating a class function on conjugacy classes

Let $G$ be a group and $k$ a
field. For every class function $f : G \to k$ and every $x \in G$, the function on
conjugacy classes that corresponds to $f$ under the linear isomorphism between class
functions and functions on conjugacy classes takes the value $f(x)$ at the conjugacy
class of $x$.

Formalized by `MathlibExt.GroupTheory.ClassFunctionWanted.classFunctionsEquivConjClasses_apply_mk`, a theorem declared in [MathlibExt/GroupTheory/ClassFunction.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassFunction.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#class-functions-equiv-conj-classes-apply).

## Lifting a function on conjugacy classes

Let $G$ be a group and $k$ a field. For
every function $q$ from the set of conjugacy classes of $G$ to $k$ and every $x \in G$,
the class function that corresponds to $q$ under the inverse of the linear isomorphism
between class functions and functions on conjugacy classes takes at $x$ the value of $q$
at the conjugacy class of $x$.

Formalized by `MathlibExt.GroupTheory.ClassFunctionWanted.classFunctionsEquivConjClasses_symm_apply`, a theorem declared in [MathlibExt/GroupTheory/ClassFunction.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassFunction.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#class-functions-equiv-conj-classes-symm).

## Dimension of the space of class functions

Let $G$ be a finite group and $k$ a field.
The space of class functions $G \to k$ is a $k$-vector space whose dimension equals the
number of conjugacy classes of $G$.

Proof: The linear isomorphism between class functions and functions on conjugacy classes
reduces this to the space of all functions from the finite set of conjugacy classes of
$G$ to $k$, whose dimension is the number of conjugacy classes.

## Sources

- J.-P. Serre, Linear Representations of Finite Groups, GTM 42, §2.7, Theorem 6 (dimension count for class functions).

Formalized by `MathlibExt.GroupTheory.ClassFunctionWanted.finrank_classFunctions_eq_card_conjClasses`, a theorem declared in [MathlibExt/GroupTheory/ClassFunction.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/ClassFunction.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#finrank-class-functions-eq-card-conj-cla).

## Irreducible representations are simple objects

Let $k$ be a field, $G$ a group and
$\rho$ an irreducible representation of $G$ on a finite-dimensional $k$-vector space $V$. Then
$\rho$, viewed as an object of the category of finite-dimensional representations of $G$ over
$k$, is a simple object.

Formalized by `FDRep.simple_of_isIrreducible`, a theorem declared in [MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#simple-of-is-irreducible).

## Characters of nonisomorphic simple representations are linearly independent

Let $G$ be
a finite group and let $(V_i)_{i \in I}$ be a family of simple finite-dimensional complex
representations of $G$ such that $V_i \cong V_j$ implies $i = j$. Then the characters of the
$V_i$ are linearly independent over $\mathbb{C}$.

Formalized by `FDRep.linearIndependent_character`, a theorem declared in [MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#linear-independent-character).

## A class function orthogonal to all irreducible characters vanishes

Let $G$ be a finite
group and let $f : G \to \mathbb{C}$ satisfy $f(hgh^{-1}) = f(g)$ for all $g, h \in G$. Suppose
that for every simple finite-dimensional complex representation $W$ of $G$, with character
$\chi_W$,

$$\frac{1}{|G|} \sum_{g \in G} f(g)\, \chi_W(g^{-1}) = 0.$$

Then $f = 0$.

Formalized by `FDRep.eq_zero_of_isClassFunction_of_orthogonal`, a theorem declared in [MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#eq-zero-of-is-class-function-of-orthogon).

## Irreducible characters are linearly independent

Let $G$ be a finite group. The irreducible
complex characters of $G$, that is, the functions $G \to \mathbb{C}$ that are the character of
some simple finite-dimensional complex representation of $G$, are linearly independent over
$\mathbb{C}$ in the space of functions $G \to \mathbb{C}$.

Proof: Apply row orthogonality (C. Teleman, *Representation Theory*, Cambridge lecture
notes, 2005, Theorem 8.10) as coordinate functionals to a vanishing finite linear
combination of pairwise distinct irreducible characters.

## Sources

- J.-P. Serre, Linear Representations of Finite Groups, GTM 42, §2.5 (independence of irreducible characters).

Formalized by `MathlibExt.GroupTheory.IrreducibleCharacterBasisWanted.linearIndependent_irrCharacters`, a theorem declared in [MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean, line 514](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean#L514). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#linear-independent-irr-characters).

## Irreducible characters span the class functions

Let $G$ be a finite group and let
$f : G \to \mathbb{C}$ satisfy $f(hgh^{-1}) = f(g)$ for all $g, h \in G$. Then $f$ is a
$\mathbb{C}$-linear combination of irreducible complex characters of $G$, that is, of functions
$G \to \mathbb{C}$ that are the character of some simple finite-dimensional complex representation
of $G$.

Proof: Subtract the orthogonal projection onto the irreducible characters. The
remainder vanishes by Schur's lemma, Maschke's theorem, and the regular
representation on a small model of the complex group algebra, as in the proof of
Teleman's Theorem 9.3 (completeness of characters).

## Sources

- J.-P. Serre, Linear Representations of Finite Groups, GTM 42, §2.7, Theorem 6 (irreducible characters span the class functions).

Formalized by `MathlibExt.GroupTheory.IrreducibleCharacterBasisWanted.mem_span_irrCharacters_of_isClassFunction`, a theorem declared in [MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean, line 548](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean#L548). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#mem-span-irr-characters-of-is-class-func).

## Number of irreducible characters

Let $G$ be a finite group. The number of irreducible
complex characters of $G$, that is, of functions $G \to \mathbb{C}$ that are the character of
some simple finite-dimensional complex representation of $G$, equals the number of conjugacy
classes of $G$.

Proof: The irreducible characters are linearly independent and span the class functions, so
they form a basis of that space; compare its cardinality with the known dimension of that
space (P. Etingof et al., *Introduction to representation theory*, arXiv:0901.0827,
Theorem 3.5 and Corollary 3.6).

## Sources

- J.-P. Serre, Linear Representations of Finite Groups, GTM 42, §2.7 (number of irreducible characters).

Formalized by `MathlibExt.GroupTheory.IrreducibleCharacterBasisWanted.card_irrCharacters_eq_card_conjClasses`, a theorem declared in [MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean, line 635](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/IrreducibleCharacterBasis.lean#L635). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html#card-irr-characters-eq-card-conj-classes).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Irreducible characters and class functions](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/characters-of-finite-groups/irreducible-characters-and-class-functions)
