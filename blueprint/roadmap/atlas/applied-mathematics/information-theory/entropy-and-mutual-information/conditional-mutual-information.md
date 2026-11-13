---
declaration: section
origin: cited
lean: InformationTheory.sum_toReal_mul_comp, InformationTheory.le_map_apply, InformationTheory.toReal_le_map_apply, InformationTheory.shannonEntropy_mul_log_two, InformationTheory.sum_mul_log_map, InformationTheory.shannonEntropy_map_equiv_comp, InformationTheory.finiteMutualInformation, InformationTheory.finiteMutualInformation_eq
statement: formalized
proof: formalized
---

# Conditional mutual information

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html).

## Sums against a pushforward of a finite law

Summing a function of `f t` against `p` is summing against the pushforward `p.map f`.

Formalized by `InformationTheory.sum_toReal_mul_comp`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#sum-to-real-mul-comp).

## Atom mass is at most the mass of its image

An atom's mass is at most the mass of its image.

Formalized by `InformationTheory.le_map_apply`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#le-map-apply).

## Atom mass is at most the mass of its image, in reals

An atom's mass is at most the mass of its image, as real numbers.

Formalized by `InformationTheory.toReal_le_map_apply`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#to-real-le-map-apply).

## Shannon entropy as a p log p sum

Entropy times `log 2` as a `p log p` sum.

Formalized by `InformationTheory.shannonEntropy_mul_log_two`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#shannon-entropy-mul-log-two).

## Log-sum against a pushforward equals its negative entropy

`∑ p(t) log (p.map f)(f t) = -H(p.map f) log 2`.

Formalized by `InformationTheory.sum_mul_log_map`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#sum-mul-log-map).

## Entropy of a pushforward is invariant under relabeling

Relabeling the image of a map by a bijection preserves entropy.

Formalized by `InformationTheory.shannonEntropy_map_equiv_comp`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#shannon-entropy-map-equiv-comp).

## Mutual information of a finite joint law

Mutual information `I(X; Y)` of a finite joint law `p` of `(X, Y)`, in bits: the real value
of `measureMutualInformation` on `p`, which is finite here (`finiteMutualInformation_eq`). Each
finite alphabet carries the discrete σ-algebra.

Formalized by `InformationTheory.finiteMutualInformation`, a definition declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#finite-mutual-information).

## Mutual information in terms of entropies

`I(X; Y) = H(X) + H(Y) - H(X, Y)` for a finite joint law.

Formalized by `InformationTheory.finiteMutualInformation_eq`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#finite-mutual-information-eq).

## Conditional mutual information of a finite joint law

The conditional mutual information `I(X; Y | Z)` of a finite joint law `p` of `(X, Y, Z)`, in
bits: `∑ p(x, y, z) log₂ (p(x, y, z) p(z) / (p(x, z) p(y, z)))`.

Formalized by `InformationTheory.finiteConditionalMutualInformation`, a definition declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#finite-conditional-mutual-information).

## Conditional mutual information in terms of entropies

`I(X; Y | Z) = H(X, Z) + H(Y, Z) - H(X, Y, Z) - H(Z)`.

Formalized by `InformationTheory.finiteConditionalMutualInformation_eq`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#finite-conditional-mutual-information-eq).

## Nonnegativity of conditional mutual information

Conditional mutual information is nonnegative.

Formalized by `InformationTheory.finiteConditionalMutualInformation_nonneg`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#finite-conditional-mutual-information-no).

## Vanishing conditional mutual information iff conditional independence

`I(X; Y | Z) = 0` exactly when `X` and `Y` are conditionally independent given `Z`:
`p(x, y, z) p(z) = p(x, z) p(y, z)` for every atom.

Formalized by `InformationTheory.finiteConditionalMutualInformation_eq_zero_iff`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#finite-conditional-mutual-information-eq-2).

## Chain rule for mutual information

`I(X; (Y, Z)) = I(X; Z) + I(X; Y | Z)`. Here `p` is
read as a joint law of `X` and the pair `(Y, Z)`.

Formalized by `InformationTheory.finiteMutualInformation_chain_rule`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#finite-mutual-information-chain-rule).

## Data-processing inequality

**Data-processing inequality**, first half: if `X` and `Z` are conditionally independent given
`Y` (a Markov chain `X - Y - Z`, stated as `I(X; Z | Y) = 0` for the joint law `p` of
`(X, Y, Z)`), then `I(X; Z) ≤ I(X; Y)`.

Formalized by `InformationTheory.finiteMutualInformation_le_left_of_markov`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#finite-mutual-information-le-left-of-mar).

## Data-processing inequality

**Data-processing inequality**, second half: under the same Markov condition,
`I(X; Z) ≤ I(Y; Z)`.

Formalized by `InformationTheory.finiteMutualInformation_le_right_of_markov`, a theorem declared in [MathlibExt/InformationTheory/ConditionalMutualInformation.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/ConditionalMutualInformation.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html#finite-mutual-information-le-right-of-ma).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conditional mutual information](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/entropy-and-mutual-information/conditional-mutual-information)
