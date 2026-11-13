---
declaration: section
origin: cited
lean: Cslib.Language.regularStarHeight, Cslib.Language.GenRegExp, Cslib.Language.GenRegExp.denote, Cslib.Language.GenRegExp.starHeight, Cslib.Language.HasGenHeightLe
statement: formalized
proof: formalized
---

# Star height

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/star-height/index.html).

## Language

## Star height of a regular expression

The star height of an ordinary regular expression
is the nesting depth of the Kleene star in it: the expressions for the empty language and the
empty word and the single letters have star height $0$; a union $e_1 + e_2$ and a concatenation
$e_1 e_2$ have the larger of the star heights of $e_1$ and $e_2$; and $e^*$ has star height one
more than $e$.

Formalized by `Cslib.Language.regularStarHeight`, a definition declared in [CSLibExt/Computability/Languages/GeneralizedRegularExpression.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/GeneralizedRegularExpression.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/star-height/index.html#regular-star-height).

## Generalized regular expressions

A generalized regular expression over an alphabet
$\alpha$ is built from ordinary regular expressions over $\alpha$ by complement, union,
concatenation and Kleene star: every ordinary regular expression over $\alpha$ is one, and if
$e$, $e_1$, $e_2$ are generalized regular expressions, then so are the complement $\neg e$, the
union $e_1 + e_2$, the concatenation $e_1 e_2$ and the star $e^*$.

Formalized by `Cslib.Language.GenRegExp`, an inductive type declared in [CSLibExt/Computability/Languages/GeneralizedRegularExpression.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/GeneralizedRegularExpression.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/star-height/index.html#gen-reg-exp).

## Language of a generalized regular expression

For an alphabet $\alpha$, the language over
$\alpha$ denoted by a generalized regular expression over $\alpha$ is defined recursively, for
generalized regular expressions $e$, $e_1$, $e_2$: an ordinary regular expression denotes the
language it matches; the complement $\neg e$ denotes the complement, in the set of all words over
$\alpha$, of the language of $e$; the union $e_1 + e_2$ denotes the union and the concatenation
$e_1 e_2$ the concatenation of the languages of $e_1$ and $e_2$; and the star $e^*$ denotes the
Kleene star of the language of $e$.

Formalized by `Cslib.Language.GenRegExp.denote`, a definition declared in [CSLibExt/Computability/Languages/GeneralizedRegularExpression.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/GeneralizedRegularExpression.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/star-height/index.html#denote).

## Generalized star height

The generalized star height of a generalized regular expression
is the nesting depth of the Kleene star in it, counting the stars inside its ordinary regular
subexpressions: for generalized regular expressions $e$, $e_1$, $e_2$, an ordinary regular
expression has its usual star height; the complement $\neg e$ has the star height of $e$; the
union $e_1 + e_2$ and the concatenation $e_1 e_2$ have the larger of the star heights of $e_1$
and $e_2$; and the star $e^*$ has star height one more than $e$.

Formalized by `Cslib.Language.GenRegExp.starHeight`, a definition declared in [CSLibExt/Computability/Languages/GeneralizedRegularExpression.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/GeneralizedRegularExpression.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/star-height/index.html#star-height).

## Bounded generalized star height

A language $L$ over an alphabet $\alpha$ has generalized
star height at most $n$, for a natural number $n$, if some generalized regular expression over
$\alpha$ whose generalized star height is at most $n$ denotes $L$.

Formalized by `Cslib.Language.HasGenHeightLe`, a definition declared in [CSLibExt/Computability/Languages/GeneralizedRegularExpression.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/GeneralizedRegularExpression.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/star-height/index.html#has-gen-height-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Star height](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/star-height/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/regular-languages/automata-and-expressions/star-height)
