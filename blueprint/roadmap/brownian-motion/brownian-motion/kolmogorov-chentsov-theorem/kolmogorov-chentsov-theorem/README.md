# Kolmogorov-Chentsov Theorem

## Sets with bounded internal covering number

TODO: change the proofs here to avoid $s \ne t$ and use instead properties of processes satisfying the Kolmogorov condition for exponents $(p,q)$.

- [integral_div_dist_le_sum_integral_dist_le](lem-integral-div-dist-le-sum-integral-dist-le.md)
- [L](def-l.md)
- [L_lt_top](lem-l-lt-top.md)
- [finite_set_bound](lem-finite-set-bound.md)
- [countable_set_bound](thm-countable-set-bound.md)
- [holder_modification_single](lem-holder-modification-single.md)
- [holder_modification](thm-holder-modification.md)

## Localized Kolmogorov-Chentsov theorem

- [Cover with bounded covering numbers](def-hasboundedcoveringnumbercover.md)
- [hasBoundedCoveringNumberCover_nnreal](lem-hasboundedcoveringnumbercover-nnreal.md)

Note: in the Lean code, we proved this result for weaker constants: $c_n = 3n$.

*The proof of [Lemma hasBoundedCoveringNumberCover_nnreal](lem-hasboundedcoveringnumbercover-nnreal.md) is shown with its statement.*

We say that a function is *locally* Hölder continuous of order $\gamma$ if for any point $x$ in its domain there is a neighborhood of $x$ on which the function is Hölder continuous of order $\gamma$.

- [localized_holder_modification](thm-localized-holder-modification.md)
- [localized_holder_modification_sup](thm-localized-holder-modification-sup.md)
