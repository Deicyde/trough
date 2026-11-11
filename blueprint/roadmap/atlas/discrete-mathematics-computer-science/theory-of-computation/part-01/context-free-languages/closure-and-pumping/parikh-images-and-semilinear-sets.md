---
declaration: section
origin: cited
lean: Cslib.Language.parikhVector, Cslib.Language.parikhImage, Cslib.Language.parikhVector_nil, Cslib.Language.parikhVector_append, Cslib.Language.parikhImage_union, Cslib.Language.parikhImage_empty, Cslib.Language.parikhImage_singleton, Cslib.Language.linComb
statement: formalized
proof: formalized
---

# Parikh images and semilinear sets

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html).

## Parikh vector of a word

The Parikh vector of a word: the function counting, for each
letter, how many times it occurs in the word.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.parikhVector`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#parikh-vector).

## Parikh image of a language

The Parikh image of a language: the set of Parikh vectors of its
words.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.parikhImage`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#parikh-image).

## Parikh vector of the empty word is zero

The Parikh vector of the empty word is zero.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.parikhVector_nil`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#parikh-vector-nil).

## Parikh vectors add over concatenation

Parikh vectors add over concatenation.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.parikhVector_append`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#parikh-vector-append).

## Parikh image of a union of languages

The Parikh image of a union is the union of the Parikh images.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.parikhImage_union`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#parikh-image-union).

## Parikh image of the empty language is empty

The Parikh image of the empty language is empty.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.parikhImage_empty`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#parikh-image-empty).

## Parikh image of a singleton language

The Parikh image of a singleton language is the singleton of the
Parikh vector.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.parikhImage_singleton`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#parikh-image-singleton).

## Linear combination of period vectors

The linear combination of a list of period vectors with a
coefficient list `c`: pair the two lists position by position and
sum the scaled periods, and reject mismatched lengths by
returning `0` (the length guard is checked up front, before the
recursion, so a shorter coefficient list cannot silently truncate
and a longer one cannot silently drop coefficients). Coefficients
are indexed by *position* in `P`, not by period value, so duplicate
periods get independent coefficients: for `P = [p, p]`,
`linComb P [1, 0] = p`, not `2 • p`.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.linComb`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#lin-comb).

## Unguarded linear combination agrees on equal lengths

The unguarded recursion agrees with `linComb` on equal-length
inputs.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.linComb_eq_aux_of_length_eq`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#lin-comb-eq-aux-of-length-eq).

## Linear combination with too few coefficients is zero

Mismatched lengths are rejected: a shorter coefficient list
does not silently truncate.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.linComb_eq_zero_of_length_lt`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#lin-comb-eq-zero-of-length-lt).

## Linear combination with too many coefficients is zero

Mismatched lengths are rejected: a longer coefficient list
does not silently drop coefficients.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.linComb_eq_zero_of_length_gt`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#lin-comb-eq-zero-of-length-gt).

## Duplicate periods get independent coefficients

Duplicate periods get independent coefficients: with
`P = [p, p]`, the coefficients `(1, 0)` give `p`.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.linComb_dup`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#lin-comb-dup).

## Linear set of vectors

A set of vectors is linear when it consists of a base vector plus
arbitrary nonnegative combinations of finitely many period vectors,
with one coefficient per position in the period list.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.IsLinear`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#is-linear).

## Semilinear set of vectors

A set of vectors is semilinear when it is a finite union of
linear sets.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.IsSemilinear`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#is-semilinear).

## A singleton set of vectors is linear

A singleton set of vectors is linear, with no periods.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.isLinear_singleton`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#is-linear-singleton).

## Linear sets are semilinear

Linear sets are semilinear.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.IsLinear.isSemilinear`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#is-semilinear-2).

## The empty set is semilinear

The empty set of vectors is semilinear.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.isSemilinear_empty`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#is-semilinear-empty).

## A singleton set of vectors is semilinear

A singleton set of vectors is semilinear.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.isSemilinear_singleton`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#is-semilinear-singleton).

## Semilinear sets are closed under union

Semilinear sets are closed under union.

## Sources

- Parikh, "On context-free languages", Journal of the ACM 13 (1966), 570-581.

Formalized by `Cslib.Language.IsSemilinear.union`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Parikh.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Parikh.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html#union).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parikh images and semilinear sets](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/parikh-images-and-semilinear-sets)
