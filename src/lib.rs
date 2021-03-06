use ndarray::Array2;
use numpy::{PyArray2, ToPyArray};
use pyo3::prelude::*;
use pyo3::{types::PyList, wrap_pyfunction};

fn calc_spt(spt_i: &Vec<f64>, spt_j: &Vec<f64>) -> f64 {
    let mut val = 0.0;

    for (attr_i, attr_j) in spt_i.iter().zip(spt_j.iter()) {
        val += attr_i * attr_j;
    }

    val
}

fn calc_param_spt(spt_i: &(i64, i64, f64), spt_j: &(i64, i64, f64)) -> f64 {
    (((spt_i.0 - spt_j.0) + (spt_i.1 - spt_j.1)) as f64) / (spt_i.2 + spt_j.2)
}

#[pyfunction]
fn construct_calc_mat<'a>(
    py: Python<'a>,
    spt_params: &'a PyList,
) -> &'a PyArray2<f64> {
    let param_vec = spt_params.extract::<Vec<Vec<f64>>>().unwrap();
    let l = param_vec.len();

    let mut arr: Array2<f64> = Array2::zeros((l, l));

    for i in 0..l {
        for j in 0..l {
            arr[[i, j]] = calc_spt(&param_vec[i], &param_vec[j]);
        }
    }

    arr.to_pyarray(py)
}

#[pyfunction]
fn construct_param_mat<'a>(
    py: Python<'a>,
    spt_params: &'a PyList,
) -> &'a PyArray2<f64> {
    let param_vec = spt_params.extract::<Vec<(i64, i64, f64)>>().unwrap();
    let l = param_vec.len();

    let mut arr: Array2<f64> = Array2::zeros((l, l));

    for i in 0..l {
        for j in 0..l {
            arr[[i, j]] = calc_param_spt(&param_vec[i], &param_vec[j]);
        }
    }

    arr.to_pyarray(py)
}

#[pymodule]
fn spt_lib(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(construct_calc_mat))?;
    m.add_wrapped(wrap_pyfunction!(construct_param_mat))?;

    Ok(())
}
