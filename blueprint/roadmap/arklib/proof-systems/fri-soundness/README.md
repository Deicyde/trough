# FRI soundness

We follow the March 27, 2026 revision of ([Garreta et al. 2025](https://eprint.iacr.org/2025/1993)). The earlier [zkSecurity formalization](https://github.com/zksecurity/simple-rbr-fri), by Yoichi Hirai and Harmonic's Aristotle, with subsequent work by Pietro Monticone, also informed the argument. ArkLib reuses its existing Reed–Solomon codes, word-folding operations, mutual correlated agreement (MCA), and probability theory.

Let $D$ be a multiplicative coset of size $2^n$, let $m=2^k$ be a folding factor, and let $D'=D^m$. Write $C=\mathrm{RS}(D,md)$ and $C'=\mathrm{RS}(D',d)$, with $d>0$. For a word $f$ on $D$, write $f_j$ for the coefficient words of its block interpolants, so that $\operatorname{Fold}_\alpha(f)=\sum_{j\lt m}\alpha^j f_j$.

- [fri-coefficient-lift](lem-fri-coefficient-lift.md)
- [fri-folding-failure](def-fri-folding-failure.md)
- [fri-folding-error](thm-fri-folding-error.md)
- [fri-query-error](thm-fri-query-error.md)
- [fri-binding](thm-fri-binding.md)
- [fri-soundness](thm-fri-soundness.md)

Executable specification and scope. The executable local consistency check is related to ArkLib's word fold by `RoundConsistency.roundConsistencyCheck_eq_foldValue`, for arbitrary oracle words. The specification retains all prior words, and checks the final polynomial's degree before the query phase. `Fri.Spec.reduction_run` identifies the exact acceptance event of `Fri.Spec.reduction`; the input-language bridge uses its original computational-polynomial witness relation. The result concerns the interactive oracle protocol, not Fiat–Shamir compilation or a concrete commitment scheme.

## Certified straightline extraction

Write $N=2^n$, $b_i=2^{s_i}$, and $M=(\prod_i b_i)d$ for the initial polynomial dimension, where all folding exponents and $d$ are positive and $\sum_i s_i\leq n$. The retained history contains arbitrary committed words, the folding challenges, and a final computational polynomial. No intermediate honesty assumption is made.

- [fri-measured-extractor](def-fri-measured-extractor.md)
- [fri-extractor-recovery](thm-fri-extractor-recovery.md)
- [fri-knowledge-soundness](thm-fri-knowledge-soundness.md)

Resource model. The arithmetic and immutable-input instruction handlers execute the very program whose result defines the extractor. Field nodes are generated from at most two domain reads by explicit measured powers; word-read addresses carry those nodes. The profiles count repeated word, domain, challenge, coefficient, and cached-array accesses; field addition, subtraction, multiplication, equality, and inversion; and designated source-level control ticks. An inverse is one algebraic primitive. Erased certificates carry the reference-domain and polynomial identities. These counts exclude receipt or deserialization of retained functions, the cost of evaluating those functions, allocation, machine index arithmetic, and field bit complexity. Complete index enumeration prevents a claim of total $O(M)$ workspace here. The algebraic interpolation theorem above remains a separate statement from these explicit measured programs.

- [fri-extractor-resources](thm-fri-extractor-resources.md)

Under the actual reduction's $M\leq N$ constraint, these envelopes are polynomial in $N$, rather than in $\log N$. The unit-access model above does not bound bit complexity or cryptographic polynomial running time.
