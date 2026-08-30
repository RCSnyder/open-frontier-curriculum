---
title: "Linear algebra"
wave: 1
order: 3
leverage: 99
---

# Linear algebra

<div class="grid cards ofc-compact" markdown>

- **Prerequisites**  
  Modules 1-2 can overlap

- **Exit capability**  
  Own vector spaces, projections, least squares, matrix maps, rank/nullspace, conditioning, SVD/eigenstructure.

- **Unlocks / transfers to**  
  ML; control; estimation; quantum; signals; robotics; materials simulation; computational biology.

</div>

## Weeks

### Week 10

**Spine:** Boyd & Vandenberghe, Introduction to Applied Linear Algebra

**Reading:** Ch. 1-3, pp. 1-68: vectors; linear functions; norm/distance

**Know:** Represent state/data as vectors; use norms, inner products, angles and linear maps.

**Reconstruct:** Derive Cauchy-Schwarz geometrically; derive projection onto a vector.

**Do:** Represent a multi-sensor robot state and design three different norms; show how each changes what 'closest state' means.

**Defend:** Why is the choice of norm a modeling decision, not merely notation?

**Gate:** Closed-book vector identities + one modeling problem where units differ across coordinates.

**Source:** [source](https://stanford.edu/~boyd/vmls/)

### Week 11

**Spine:** Boyd & Vandenberghe, Introduction to Applied Linear Algebra

**Reading:** Ch. 5-6, approx. pp. 89-128: linear independence; matrices

**Know:** Diagnose redundancy, basis choice, rank and matrix-as-map thinking.

**Reconstruct:** Regenerate definitions of independence/span/basis; prove uniqueness of coordinates in a basis.

**Do:** Construct a sensor matrix with deliberate redundancy; identify which sensor combinations are informationally redundant.

**Defend:** What is the operational meaning of rank loss?

**Gate:** reduce an unseen matrix model to independent degrees of freedom and defend the basis.

**Source:** [source](https://stanford.edu/~boyd/vmls/)

### Week 12

**Spine:** Boyd & Vandenberghe, Introduction to Applied Linear Algebra

**Reading:** Ch. 8-11, pp. 147-224: linear equations; linear dynamical systems; multiplication; inverses

**Know:** Solve linear systems; reason about reachability over repeated matrix dynamics; interpret inverses and condition.

**Reconstruct:** Derive solution conditions for Ax=b in terms of span; derive x(t)=A^t x(0) for a discrete linear system.

**Do:** Model a 4-compartment resource flow system and explore stable, unstable, and conserved modes numerically.

**Defend:** Why can an inverse exist mathematically yet be useless numerically?

**Gate:** Closed-book solve + condition/sensitivity explanation on an almost-singular system.

**Source:** [source](https://stanford.edu/~boyd/vmls/)

### Week 13

**Spine:** Boyd & Vandenberghe, Introduction to Applied Linear Algebra

**Reading:** Ch. 12-13, pp. 225-284: least squares; data fitting

**Know:** Derive least squares as projection; understand residual orthogonality and regression geometry.

**Reconstruct:** Derive normal equations from minimizing ||Ax-b||² and derive QR-based solution conceptually.

**Do:** Fit a calibration curve with outliers; compare normal equations and QR numerically.

**Defend:** What exactly is being optimized in least squares, and what assumptions make that meaningful?

**Gate:** derive least squares two ways (geometry + calculus) and identify when both views fail.

**Source:** [source](https://stanford.edu/~boyd/vmls/)

### Week 14

**Spine:** Boyd & Vandenberghe, Introduction to Applied Linear Algebra + supplement

**Reading:** Ch. 16 constrained least squares, pp. 339-356; Ch. 18 nonlinear least squares, pp. 381-418; supplement eigen/SVD from FNC Ch. 7

**Know:** Handle constraints, nonlinear fitting, SVD/eigenstructure, low-rank approximation and ill-conditioning.

**Reconstruct:** Derive rank-1 SVD approximation intuition; derive Gauss-Newton linearization for nonlinear least squares.

**Do:** Compress a synthetic sensor dataset with SVD and quantify reconstruction/error tradeoff; then fit a nonlinear model.

**Defend:** Why are small singular values simultaneously useful information and a numerical warning?

**Gate:** diagnose rank, conditioning, identifiability and compression on a fresh dataset.

**Source:** [source](https://stanford.edu/~boyd/vmls/)

## Exit gate

**Closed-book:** 120 min: projection, least squares, rank/nullspace, basis, eigenmode and SVD questions.

**Novel problem:** Given an unknown sensor/actuator matrix, diagnose redundancy, identifiability and conditioning.

**Artifact:** Implement QR least squares + SVD diagnostic; compare against naive inverse/normal equations.

**Defend:** Explain rank loss, small singular values, basis dependence and coordinate-invariant statements.

**Pass criterion:** Pass if learner predicts numerical failure before running code and justifies representation choices.

## Transfer problems

Try these before consulting solutions or asking for the complete answer.

1. **Projection**: Project an observation onto a model subspace and interpret the residual physically.

2. **Rank**: Create a matrix whose columns look different but are linearly dependent; explain the hidden redundancy.

3. **Nullspace**: Find a nonzero actuator command that produces zero net output in a toy mechanism.

4. **Conditioning**: Construct two nearly collinear columns and measure solution sensitivity to 0.1% data perturbation.

5. **Dynamics**: Analyze repeated x_{k+1}=Ax_k for modes that decay, persist, or grow.

6. **Least squares**: Fit an overdetermined calibration system and verify residual orthogonality.

7. **QR vs normal**: Solve the same ill-conditioned least-squares problem both ways and compare.

8. **SVD**: Find the best rank-1 approximation to a small dataset and quantify lost variance/information.

9. **Identifiability**: Given y=Ax with fewer independent measurements than state dimensions, describe all indistinguishable states.

10. **Constraints**: Solve a constrained least-squares allocation problem and interpret active constraints.

## Textbooks

See the [five-book resource page](../../07-resources/textbooks/linear-algebra.md).
