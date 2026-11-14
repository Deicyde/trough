---
navigation: transparent
---

# statInfo to tvDist_eq_integral_abs

- [statInfo](def-statinfo.md)

The statistical information is the difference between the minimal risk of an estimator that does not depend on the data and that of a Bayes estimator. This is a simple generalization of both the DeGroot statistical information as well as the hockey-stick (or $E_\gamma$) divergence.

- [statInfo_self](lem-statinfo-self.md)
- [statInfo_le](lem-statinfo-le.md)
- [statInfo_symm](lem-statinfo-symm.md)
- [Data-processing inequality](thm-data-proc-statinfo.md)
- [statInfo_data_proc_event](cor-statinfo-data-proc-event.md)
- [statInfo_eq_sub_min](lem-statinfo-eq-sub-min.md)
- [statInfo_eq_integral_abs_sub](lem-statinfo-eq-integral-abs-sub.md)
- [Integral form of the statistical information](thm-statinfo-eq-integral.md)

For probability measures, this theorem makes the statistical information an $f$-divergence (which is defined later in this document).

*The proof of [Integral form of the statistical information](thm-statinfo-eq-integral.md) is shown with its statement.*

- [statInfo_eq_integral_abs](cor-statinfo-eq-integral-abs.md)
- [statInfo_eq_sub_inf_event](lem-statinfo-eq-sub-inf-event.md)
- [deGrootInfo](def-degrootinfo.md)
- [eGamma](def-egamma.md)

Note that our definition of the $E_\gamma$ divergence extends the one from the literature: the divergence is usually defined for $\gamma \ge 1$ only. The extension makes sense in light of Theorem [fDiv_eq_integral_eGamma](../../f-divergences/part-02/thm-fdiv-eq-integral-egamma.md). It is also extended from probability measures to finite measures.

## Total variation distance

- [TV](def-tv.md)

This is also equal to $2 I_{1/2}(\mu, \nu)$ and to $E_1(\mu, \nu)$.

- [tv_self](lem-tv-self.md)
- [tv_nonneg](lem-tv-nonneg.md)
- [tv_le](lem-tv-le.md)
- [Data-processing inequality](thm-tv-data-proc.md)
- [Total variation distance of Mathlib](def-tvdist.md)
- [tvDist_eq_integral_abs](lem-tvdist-eq-integral-abs.md)
