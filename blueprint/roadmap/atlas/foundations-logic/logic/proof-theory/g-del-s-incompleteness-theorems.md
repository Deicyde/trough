---
declaration: section
origin: cited
lean: MetaMathlibExt.godel_rosser_abstract_schema, MetaMathlibExt.hilbert_bernays_lob_second_incompleteness
statement: formalized
proof: formalized
---

# Gödel's incompleteness theorems

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/g-del-s-incompleteness-theorems/index.html).

## Abstract Gödel–Rosser incompleteness theorem

Let $\mathcal{L}$ be a set of formulas with
operations $\neg$ and $\to$, a substitution map sending $A \in \mathcal{L}$ and $n \in \mathbb{N}$
to $A[n] \in \mathcal{L}$, a coding map $\ulcorner \cdot \urcorner : \mathcal{L} \to \mathbb{N}$,
a formula $R \in \mathcal{L}$, predicates "provable" (written $\vdash A$), "Rosser provable" and
"true" on $\mathcal{L}$, and a proof relation $\mathrm{Prf}(A, n)$ between formulas $A$ and
natural numbers $n$. Assume that, for all formulas $A$, $B$ and all $n$:
(i) $\neg A$ is true if and only if $A$ is not true;
(ii) if $\vdash A \to B$ and $\vdash A$, then $\vdash B$;
(iii) $\vdash A$ and $\vdash \neg A$ do not both hold;
(iv) $(\neg A)[n] = \neg (A[n])$;
(v) $\vdash A$ if and only if $\mathrm{Prf}(A, k)$ for some $k$;
(vi) $A$ is Rosser provable if and only if there is $k$ with $\mathrm{Prf}(A, k)$ and there is no
$m < k$ with $\mathrm{Prf}(\neg A, m)$;
(vii) $R[\ulcorner A \urcorner]$ is true if and only if $A$ is Rosser provable;
(viii) if $A$ is Rosser provable, then $\vdash R[\ulcorner A \urcorner]$;
(ix) if $\vdash \neg A$, then $\vdash \neg R[\ulcorner A \urcorner]$;
(x) for every formula $F$ there is a formula $G$ with $G[k] = G$ for all $k$,
$\vdash G \to F[\ulcorner G \urcorner]$ and $\vdash F[\ulcorner G \urcorner] \to G$, such that
$G$ is true if and only if $F[\ulcorner G \urcorner]$ is true.
Then there is a formula $G$ with $G[k] = G$ for all $k$ such that $G$ is true, $\nvdash G$ and
$\nvdash \neg G$.

These hypotheses are assumed as an interface; they are not derived from a concrete effective
arithmetic syntax.

Proof: Apply diagonalization to the negation of the Rosser provability formula, then use
consistency and representability as in Rosser (1936) and Smith, 2nd ed., Chapter 25.

## Sources

- Kurt Gödel, *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I*, Monatshefte für Mathematik und Physik 38 (1931), 173–198; J. Barkley Rosser, *Extensions of some theorems of Gödel and Church*, Journal of Symbolic Logic 1 (1936), 87–91.

Formalized by `MetaMathlibExt.godel_rosser_abstract_schema`, a theorem declared in [MathlibExt/Logic/GodelRosserAbstractSchema.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Logic/GodelRosserAbstractSchema.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/g-del-s-incompleteness-theorems/index.html#godel-rosser-abstract-schema).

## Gödel's second incompleteness theorem, abstract Hilbert–Bernays–Löb form

Let $\mathcal{L}$
be a set of sentences with an implication $\to$, a sentence $\bot$, a negation satisfying
$\neg A = (A \to \bot)$ for all $A$, and a provability operator
$\Box : \mathcal{L} \to \mathcal{L}$.
Let $U \vdash A$ be a relation between theories $U \subseteq \mathcal{L}$ and sentences
$A \in \mathcal{L}$ such that for every theory $U$ and all sentences $A$, $B$, $C$:
$U \vdash A \to (B \to A)$, $U \vdash (A \to (B \to C)) \to ((A \to B) \to (A \to C))$, and if
$U \vdash A \to B$ and $U \vdash A$, then $U \vdash B$. Let $T_0$ and $T$ be theories such that
$T_0 \vdash A$ implies $T \vdash A$ for every $A$, and suppose there is a sentence $G$ with
$T_0 \vdash G \to \neg \Box G$ and $T_0 \vdash \neg \Box G \to G$. Suppose that for all sentences
$A$, $B$: if $T \vdash A$, then $T \vdash \Box A$; $T \vdash \Box(A \to B) \to (\Box A \to \Box B)$;
and $T \vdash \Box A \to \Box \Box A$. Let $\mathrm{Con} = \neg \Box \bot$. If $T \nvdash \bot$,
then $T \nvdash \mathrm{Con}$.

The derivability conditions and the fixed point are assumed rather than derived from a concrete
encoding of first-order arithmetic.

Proof: Derive the needed implicational combinators from K and S, apply D1–D3 to the Gödel
fixed point $G$, and contrapose $\Box G \to \Box \bot$. This is the Hilbert–Bernays–Löb route
of Hilbert–Bernays (1939) and Löb (1955), as presented by Boolos, Ch. 3, and Smith, Ch. 33.

## Sources

- Kurt Gödel, *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I*, Monatshefte für Mathematik und Physik 38 (1931), 173–198; Martin H. Löb, *Solution of a problem of Leon Henkin*, Journal of Symbolic Logic 20 (1955), 115–118.

Formalized by `MetaMathlibExt.hilbert_bernays_lob_second_incompleteness`, a theorem declared in [MathlibExt/Logic/HilbertBernaysLob.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Logic/HilbertBernaysLob.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/g-del-s-incompleteness-theorems/index.html#hilbert-bernays-lob-second-incompletenes).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gödel's incompleteness theorems](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/g-del-s-incompleteness-theorems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/proof-theory/g-del-s-incompleteness-theorems)
