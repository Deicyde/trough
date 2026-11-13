---
declaration: section
origin: cited
lean: MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.expFunc, MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.Language.exp, MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.expRing, MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.IsSemialgebraic, MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.IsRExpDefinable, MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.algPart, MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.transPart, MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.height
statement: formalized
---

# Wilkie's conjecture

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html).

## Function symbols of the language of exponentiation

The function symbols of the language
of exponentiation, sorted by arity: there is exactly one, the unary symbol $\exp$, and there are
none of any other arity.

Formalized by `MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.expFunc`, an inductive type declared in [WantedExt/ModelTheory/WilkiesConjectureWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/ModelTheory/WilkiesConjectureWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html#exp-func).

## Language of exponentiation

The first-order language with a single function symbol, the
unary symbol $\exp$, and no relation symbols.

Formalized by `MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.Language.exp`, a definition declared in [WantedExt/ModelTheory/WilkiesConjectureWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/ModelTheory/WilkiesConjectureWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html#exp).

## Language of rings with exponentiation

The first-order language whose function symbols
are those of the language of rings, namely the binary symbols $+$ and $\cdot$, the unary symbol
$-$ and the constants $0$ and $1$, together with the unary symbol $\exp$ of the language of
exponentiation; it has no relation symbols.

Formalized by `MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.expRing`, an abbreviation declared in [WantedExt/ModelTheory/WilkiesConjectureWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/ModelTheory/WilkiesConjectureWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html#exp-ring).

## Semialgebraic set

A set $X \subseteq \mathbb{R}^n$ is semialgebraic if it is definable,
with parameters from $\mathbb{R}$, in the real numbers viewed as a structure for the language of
rings.

Formalized by `MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.IsSemialgebraic`, a definition declared in [WantedExt/ModelTheory/WilkiesConjectureWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/ModelTheory/WilkiesConjectureWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html#is-semialgebraic).

## Definable sets of the real exponential field

A set $X \subseteq \mathbb{R}^n$ is definable
in $\mathbb{R}_{\exp}$ if it is definable, with parameters from $\mathbb{R}$, in the real numbers
viewed as a structure for the language of rings with exponentiation, where the ring symbols have
their usual meaning and $\exp$ is interpreted as the real exponential function.

Formalized by `MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.IsRExpDefinable`, a definition declared in [WantedExt/ModelTheory/WilkiesConjectureWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/ModelTheory/WilkiesConjectureWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html#is-rexp-definable).

## Algebraic part of a set

For a set $X \subseteq \mathbb{R}^n$, the algebraic part
$X^{\mathrm{alg}}$ of $X$ is the union of all connected, infinite semialgebraic sets $Y$ with
$Y \subseteq X$.

The source takes the union of the connected, positive-dimensional semialgebraic subsets of $X$;
for connected semialgebraic sets, being infinite is equivalent to being positive-dimensional.

Formalized by `MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.algPart`, a definition declared in [WantedExt/ModelTheory/WilkiesConjectureWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/ModelTheory/WilkiesConjectureWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html#alg-part).

## Transcendental part of a set

For a set $X \subseteq \mathbb{R}^n$, the transcendental
part of $X$ is $X^{\mathrm{trans}} := X \setminus X^{\mathrm{alg}}$, where $X^{\mathrm{alg}}$ is
the algebraic part of $X$.

Formalized by `MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.transPart`, a definition declared in [WantedExt/ModelTheory/WilkiesConjectureWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/ModelTheory/WilkiesConjectureWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html#trans-part).

## Height of a point

For $a = (a_1, \dots, a_n) \in \mathbb{R}^n$, the height $H(a)$ is the
maximum of the absolute multiplicative Weil heights of the coordinates $a_1, \dots, a_n$. A
coordinate that is not algebraic over $\mathbb{Q}$ counts with height $1$, and for $n = 0$ the
height is $0$.

Formalized by `MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.height`, a definition declared in [WantedExt/ModelTheory/WilkiesConjectureWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/ModelTheory/WilkiesConjectureWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html#height).

## Points of bounded degree and height

For a set $X \subseteq \mathbb{R}^n$ and natural
numbers $g$ and $H$, the set $X(g, H)$ consists of the points $x = (x_1, \dots, x_n) \in X$ whose
coordinates are all algebraic over $\mathbb{Q}$, such that the field
$\mathbb{Q}(x) = \mathbb{Q}(x_1, \dots, x_n)$ satisfies $[\mathbb{Q}(x) : \mathbb{Q}] \le g$ and
the height $H(x)$ of $x$, the maximum of the absolute multiplicative Weil heights of
$x_1, \dots, x_n$ (taken to be $0$ when $n = 0$), satisfies $H(x) \le H$.

Formalized by `MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.degreeHeightLE`, a definition declared in [WantedExt/ModelTheory/WilkiesConjectureWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/ModelTheory/WilkiesConjectureWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html#degree-height-le).

## Wilkie's conjecture for the real exponential field

Let $X \subseteq \mathbb{R}^n$ be
definable in $\mathbb{R}_{\exp}$. Then there is a polynomial $f$ in two variables with real
coefficients such that the following holds for all natural numbers $g$ and $H$. Let
$X^{\mathrm{trans}}(g, H)$ be the set of points $x = (x_1, \dots, x_n)$ of the transcendental part
$X^{\mathrm{trans}}$ of $X$ whose coordinates are all algebraic over $\mathbb{Q}$, such that the
field $\mathbb{Q}(x) = \mathbb{Q}(x_1, \dots, x_n)$ satisfies $[\mathbb{Q}(x) : \mathbb{Q}] \le g$
and the height $H(x)$ of $x$, the maximum of the absolute multiplicative Weil heights of
$x_1, \dots, x_n$ (taken to be $0$ when $n = 0$), satisfies $H(x) \le H$. Then
$X^{\mathrm{trans}}(g, H)$ is finite and has at most $f(g, \log H)$ elements, where $\log 0$ is
taken to be $0$.

This is Corollary 1 of the source.

## Sources

- G. Binyamini, D. Novikov, and B. Zak, `Wilkie's conjecture for Pfaffian structures`, Annals of Math, 199 (2) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_wilkies_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.ModelTheory.WilkiesConjectureWanted.WilkiesConjecture.corollary_1` is written with `theorem_wanted` in [WantedExt/ModelTheory/WilkiesConjectureWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/ModelTheory/WilkiesConjectureWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html#corollary-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wilkie's conjecture](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/wilkie-s-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/model-theory/wilkie-s-conjecture)
