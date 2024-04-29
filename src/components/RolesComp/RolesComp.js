import React, { useState, useEffect } from 'react';
import MaterialReactTable from 'material-react-table';
import { Fragment } from 'react';
import AddItem from '../ItemsFunc/AddItem';
import { Container, Spinner } from 'react-bootstrap';
import axios from 'axios';
import { useSelector } from 'react-redux'
import DeleteItem from '../ItemsFunc/DeleteItem';
import EditItem from '../ItemsFunc/EditItem';
import { adminAuthentication } from '../LoginComp/AuthenticationFn';
import { useNavigate } from 'react-router-dom'

const RolesComp = () => {

    const navigate = useNavigate()
    const userSlice = useSelector((state) => state.user)
    const ConfigSlice = useSelector((state) => state.config)
    const name = "role"
    const hebrewName = "תפקיד"
    const [data, setData] = useState([])
    const [responseFlag, setResponseFlag] = useState(false)
    const [pagination, setPagination] = useState({
        pageIndex: 0,
        pageSize: 20
    })




    useEffect(() => {

        if (adminAuthentication(userSlice, navigate)) {
            getData()
        }
    }, [])

    const getData = async () => {
        await axios.post(`${ConfigSlice.baseUrl}/api/get_${name}`, { userSlice })
            .then(res => {
                setResponseFlag(true)
                setData(res.data.data)
            })
    }

    const emptyDict = {
        role: ""
    }


    //should be memoized or stable
    const columns = [
        {
            accessorKey: 'role',
            header: 'תפקיד',
            filterFn: (row, id, filterValue) => {
                setPagination({
                    pageIndex: 0,
                    pageSize: pagination.pageSize
                })
                return row.original[id].includes(filterValue)
            },
            muiTableHeadCellProps: {
                align: 'left',
            },
            muiTableBodyCellProps: {
                align: 'right',
            },
        }
    ]

    return (
        <Container>
            <h2 className='my'>תפקידים</h2>
            <br />
            {
                responseFlag ? (
                    <Fragment>
                        <p style={{ textAlign: "right", fontWeight: "bold" }}>בעזרת הטבלה הזאת אנו מנהלים את השמות של התפקידים הנתמכים על ידי המערכת</p>
                        <MaterialReactTable
                            columns={columns}
                            data={data}
                            initialState={{
                                columnVisibility: [],
                                showColumnFilters: true,
                                density: 'compact',
                                pagination: { pageIndex: 0, pageSize: 20 },

                            }}
                            enableEditing
                            enableRowActions
                            enableStickyHeader
                            autoResetPageIndex={false}
                            enableDensityToggle={false}
                            enableGlobalFilter={false}
                            enableColumnDragging={false}
                            paginateExpandedRows={false}
                            enableFullScreenToggle={false}
                            enableColumnActions={false}
                            enableHiding={false}
                            enableStickyFooter
                            muiTableHeadCellFilterTextFieldProps={({ column, rangeFilterIndex, table }) => {
                                return {
                                    placeholder: `חפש לפי ${column.columnDef.header}`,
                                }
                            }}
                            localization={{
                                toolbar: {
                                    searchPlaceholder: 'your string',
                                    placeholder: "sss"
                                }
                            }}
                            muiSearchTextFieldProps={{
                                placeholder: 'Search All Props',
                                sx: { minWidth: '18rem' },
                                variant: 'outlined',
                            }}
                            state={{ pagination }}
                            onPaginationChange={setPagination}
                            positionActionsColumn='last'

                            muiTablePaginationProps={{ labelRowsPerPage: `${hebrewName} בדף`, dir: "ltr" }}
                            renderRowActions={({ row }) => (
                                <div style={{ textAlign: "right" }}>
                                    <EditItem title={`עדכון ${hebrewName} קיים`} name={name} columns={columns} row={row.original} getData={getData} hebrewName={hebrewName} />
                                    <DeleteItem title={`מחיקת ${hebrewName}`} name={name} row={row.original} getData={getData} hebrewName={hebrewName} />
                                </div>
                            )}

                            renderTopToolbarCustomActions={({ table }) => {
                                return (
                                    <AddItem title={`הוספת ${hebrewName} חדש`} name={name} columns={columns} emptyDict={emptyDict} getData={getData} hebrewName={hebrewName} />
                                )
                            }}
                        />
                    </Fragment>

                ) : (<Fragment>
                    <div className='justify-content-center d-flex py-5'>
                        <h5 className='my-1'>טוען נתונים</h5>
                        <Spinner animation='border' variant='danger' className='mx-3' size='med' />
                    </div>
                </Fragment>)
            }

        </Container>

    )
};

export default RolesComp;
