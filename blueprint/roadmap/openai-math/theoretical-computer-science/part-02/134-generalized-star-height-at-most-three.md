---
declaration: section
origin: cited
lean: OAI.GeneralizedStarHeight.main
statement: formalized
proof: formalized
---

# 134. Generalized star height at most three

3 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Every regular language over a finite alphabet has a generalized regular expression with at most three nested Kleene stars, allowing union, concatenation and complement over the same alphabet. This establishes an absolute bound independent of automaton size, resolving the uniform-boundedness version of the generalized star-height problem.

## Finite Monoid Computations and a Uniform Generalized Star-Height Bound

Every regular language over a finite alphabet has a generalized regular expression of star height at most thirteen over that same alphabet. We prove this uniform bound by representing finite monoid computations as affine updates and recovering them through twelve successive split constructions.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026.pdf); the Lean below formalizes results from it.

## Generalized Star Height at Most Four

Every regular language over a finite alphabet has generalized star height at most four over that same alphabet. We give a complete construction using an affine correction that hides one interval product, a finite clock, and several scales for moving boundaries through periodic words.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/Generalized-Star-Height-at-Most-Four-September-25-2026.pdf); the Lean below formalizes results from it.

## Generalized Star Height at Most Three

Every regular language over a finite alphabet has generalized star height at most three, with complement taken in the same free monoid. We express finite-monoid computations using a prefix code of word pieces.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/article.pdf); the Lean below formalizes results from it.

## The Lean formalization

Generalized star height measures the nesting of Kleene stars in regular expressions that also allow Boolean operations. The formalization proves that every regular language over a finite alphabet has a generalized expression over the same alphabet of star height at most three. This is stronger than the bound of thirteen in the accompanying finite-monoid paper. The selected statement asserts the uniform expression bound, without separately encoding every construction step of that paper.

The formalization proves that every regular language over a finite alphabet has a generalized regular expression over that same alphabet with star height at most three. Generalized expressions allow Boolean operations as well as concatenation and Kleene star. The bound of three implies the accompanying paper's bound of four; the selected statement concerns the expression bound itself.

Generalized star height measures the nesting of Kleene stars in regular expressions that also allow Boolean operations. The formalization proves that every regular language over a finite alphabet has a generalized regular expression over that same alphabet of star height at most three. Complements are taken in the same free monoid. This is the paper's uniform bound.

## Lean: Uniform generalized star-height bound of three

Stated in [GeneralizedStarHeight.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GeneralizedStarHeight.lean).

```lean
theorem main {Alphabet : Type u} [Finite Alphabet] (L : Language Alphabet) (hL : L.IsRegular) :
    HasHeightAtMost L 3
```

Proved in [lean/OAI/Computability/StarHeight/Main.lean, line 9](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/StarHeight/Main.lean#L9).

## Lean: Generalized star height at most three

Stated in [GeneralizedStarHeight.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GeneralizedStarHeight.lean).

```lean
theorem main {Alphabet : Type u} [Finite Alphabet] (L : Language Alphabet) (hL : L.IsRegular) :
    HasHeightAtMost L 3
```

Proved in [lean/OAI/Computability/StarHeight/Main.lean, line 9](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/StarHeight/Main.lean#L9).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/134.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/134.md)
